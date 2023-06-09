defmodule D16P1 do
	#30 minutes before the volcano erupts
	#All tunnels take one minute to travel through
	#Each valve takes one minute to open

	# Step 1: Parse input.
	# Step 2: Use Floyd-Warshall Algorithm to create a distance matrix.
	# Step 3: Use DFS to solve problem.

	def read() do
		file = "input16.txt"
		{_, content} = File.read(file)
		list = String.split(content, "\r\n") |> parse_row([])
		unvisited = create_unvisited_nodes_list(list)
		map = create_hash_map(list, Map.new(), 0)
		IO.inspect(map)
		floyd_warshall(list, unvisited, map)
		# create_matrix(list)
	end

	def parse_row([], results) do
		Enum.reverse(results)
	end

	def parse_row([head|rest], results) do
		nodes = Regex.scan(~r/\s*[A-Z]{2}\s*/, head)
		|> Enum.map(fn(x) -> [y] = x; y = String.trim(y) end)
		|> List.flatten
		[node|links] = for node <- nodes do
			String.trim(node)
		end
		number = Regex.scan(~r/\d+/, head) |> List.flatten |> Enum.at(0) |> String.to_integer
		parse_row(rest, [{node, number, links}|results])
	end

	def create_unvisited_nodes_list(list) do
		Enum.filter(list, fn(x)->{_, rate, _} = x; rate > 0 end)
		|> Enum.map(fn(x)->{letter, rate, _} = x; {letter, rate} end)
	end

	#Needed to look up row and column of valve
	def create_hash_map([], map, _) do map end
	def create_hash_map([head|rest], map, acc) do
		{node, _, _} = head
		map = Map.put(map, node, acc)
		create_hash_map(rest, map, acc+1)
	end

	######################################################################################################
	# Done with parsing data. Time to implement algorithm

	def floyd_warshall(list, unvisited, map) do
		matrix = create_matrix(list)
		matrix = init_distance_of_all_immediately_adjacent(matrix, list, map)
		matrix = nested_loop(matrix, length(list))
		dfs_search(unvisited, map, matrix)
	end

	def create_matrix(list) do
		size = length(list)
		matrix = Matrix.new(size, size, nil)
		Enum.to_list(0..(size-1)) |> Enum.reduce(matrix, fn(x, acc)->Matrix.set(acc, x, x, 0) end)
	end

	def init_distance_of_all_immediately_adjacent(matrix, list, map) do
		weights = get_adjacent_valves(list, map, [])
		Enum.reduce(weights, matrix, fn(x, acc)->{row, col}=x; Matrix.set(acc, row, col, 1) end)
	end
	def get_adjacent_valves([], _, result) do List.flatten(result) end
	def get_adjacent_valves([head|rest], map, result) do
		{from, _, to} = head
		{:ok, from} = Map.fetch(map, from)
		#Fetch row, column index for valve from map
		new = for item <- to do
			{:ok, tto} = Map.fetch(map, item)
			{from, tto}
		end
		get_adjacent_valves(rest, map, [new|result])
	end

	def nested_loop(matrix, vertices) do
		loop( 0, 0, 0, vertices, matrix, :k)
	end
	#For step 3. Nested loop
	#While k < length-1, i < length-1, j < length-1
	def loop(k, i, j, length, matrix, :k) do
		matrix = loop(k, i, j, length, matrix, :i)
		cond do k < length-1 -> loop(k+1, i, j, length, matrix, :k); true -> matrix; end
	end

	def loop(k, i, j, length, matrix, :i) do
		matrix = loop(k, i, j, length, matrix, :j)
		cond do i < length-1 -> loop(k, i+1, j, length, matrix, :i); true -> matrix; end
	end

	def loop(k, i, j, length, matrix, :j) do
		a = Matrix.elem(matrix, i, j)
		b = Matrix.elem(matrix, i, k)
		c = Matrix.elem(matrix, k, j)
		matrix = case {a,b,c} do
			{nil, nil, nil} -> matrix
			{nil, nil, _} -> matrix
			{nil, _, nil} -> matrix
			{nil, _, _} -> Matrix.set(matrix, i, j, b+c)
			{_, nil, _} -> matrix
			{_, _, nil} -> matrix
			{_, _, _} -> cond do a > b + c -> Matrix.set(matrix, i, j, b+c); true -> matrix; end
		end
		cond do j < length-1 -> loop(k, i, j+1, length, matrix, :j); true -> matrix; end
	end

	# Floyd-Warshall Algorithm
	# let V = number of vetrices in graph
	# let dist = V * V array of minimum distances
	# for each vertex v
	# 	dist[v][v] <- 0
	# for each edge (u,v)
	# 	dist[u][v] <- weight(u,v)
	# for k from 1 to V
	# 	for i from 1 to V
	# 		for j from 1 to V
	# 			if dist[i][j] > dist[i][k] + dist[k][j]
	#				dist[i][j] <- dist[i][k] + dist[k][j]
	#			end if

	######################################################################################################
	# Finished creating distance matrix. Time to use DFS and solve problem.
	# Unvisited: {key, valverate}
	# List: {key, valverate, [to, to, to]}

	def dfs_search(unvisited, map, matrix) do
		node = "AA"
		Enum.each(unvisited, fn({key, valverate})->IO.puts("Key: #{key}, Rate: #{valverate}") end)
		for unvisitedNode <- unvisited do
			dfs(node, unvisitedNode, unvisited, map, matrix, 30, 0)
		end |> Enum.max()
	end

	def dfs(current_node, node, unvisited, map, matrix, time, score) when time > 0 do
		{key, valverate} = node
		{newscore, time} = add_score(current_node, key, valverate, map, matrix, time, score)
		cond do
			time < 0 -> score
			true ->
				unvisited = remove_from_unvisited(unvisited, key)
				IO.inspect(unvisited)
				case unvisited do
					[] -> newscore
					_ ->
						for unvisitedNode <- unvisited do
							dfs(key, unvisitedNode, unvisited, map, matrix, time, newscore)
						end |> Enum.max
				end
		end
	end

	def dfs(_, _, _, _, _, _, score) do
		score
	end

	def add_score(from, to, flowrate, map, matrix, time, current_score) do
		{:ok, row} = Map.fetch(map, from)
		{:ok, col} = Map.fetch(map, to)
		time_to_get_to_location = Matrix.elem(matrix, row, col)
		total_time = time_to_get_to_location + 1
		time_left = time - total_time
		score = flowrate*time_left
		{score+current_score, time_left}
	end

	def remove_from_unvisited(unvisited, remove) do
		Enum.filter(unvisited, fn(x) -> {node, _} = x; node != remove end)
	end

end
