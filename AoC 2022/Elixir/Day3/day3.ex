defmodule D3 do
  def readFile do
    file = "D:/Elixir/AdventOfCode2022inElixir/Day3/input3.txt"
    file1 = "Day3\\input3.txt"
    input = File.read(file1)
    # lines = String.split(input, "\r\n")
    # loop1(lines,0)
    #loop2(lines,0)
  end

  def loop1([], priority) do priority end
  def loop1([head|tail], priority) do
    listParts = Tuple.to_list(String.split_at(head,trunc(String.length(head)/2)))
    loop1(tail, priority + extractPriority(listParts))
  end

  def extractPriority(listParts) do
    part1 = MapSet.new(String.graphemes(Enum.at(listParts,0,nil)))
    part2 = MapSet.new(String.graphemes(Enum.at(listParts,1,nil)))
    map = MapSet.to_list(MapSet.intersection(part1,part2))
    [value] = map |> Enum.map(&String.to_charlist/1) |> List.flatten
    cond do
      65 <= value and value <= 90 -> value - 38
      97 <= value and value <= 122 -> value - 96
    end
  end

  def loop2([], priority) do priority end
  def loop2([h1,h2,h3|rest], priority) do
    part1 = MapSet.new(); part2 = MapSet.new(); part3 = MapSet.new();
    part1 = MapSet.new(String.graphemes(h1))
    part2 = MapSet.new(String.graphemes(h2))
    part3 = MapSet.new(String.graphemes(h3))
    intersection = MapSet.intersection(part1,part2)
    intersection = MapSet.intersection(intersection,part3) |> MapSet.to_list
    loop2(rest, priority + priorityFromIntersection(intersection))
  end

  def priorityFromIntersection(intersection) do

    # The code in line 48 changes the intersection from a list of strings to a list of charlists
    # using Enum.map/1 which takes the String.to_charlist/1 function as an argument which it applies
    # on the entirety of the "intersection" list. This list of charlists is then flattened
    # using the List.flatten/1 function so that all the characters are part of just one single list.

    intersection = intersection |> Enum.map(&String.to_charlist/1) |> List.flatten
    [value] = intersection
    cond do
      65 <= value and value <= 90 -> value - 38
      97 <= value and value <= 122 -> value - 96
    end
  end

  def test do
    file = "D:\\Elixir\\AdventOfCode2022\\Day3\\input3.txt"
    {:ok, input} = File.read(file)
    lines = String.split(input, "\r\n")
    IO.inspect(lines)
    h = Enum.at(lines,0,nil)
    listParts = Tuple.to_list(String.split_at(h,trunc(String.length(h)/2)))
    IO.inspect(listParts)
    part1 = MapSet.new(); part2 = MapSet.new()
    part1 = MapSet.new(String.graphemes(Enum.at(listParts,0,nil)))
    part2 = MapSet.new(String.graphemes(Enum.at(listParts,1,nil)))
    map = MapSet.to_list(MapSet.intersection(part1,part2))
    map = map |> Enum.map(&String.to_charlist/1) |> List.flatten
    [value] = map
    IO.inspect(map)
    IO.inspect(value)
    cond do
      charUpperCaseChecker(value) -> (value - 64) + 26
      true -> value - 96
    end
  end

  def test2 do
    file = "D:\\Elixir\\AdventOfCode2022\\Day3\\input3.txt"
    {:ok, input} = File.read(file)
    lines = String.split(input, "\r\n")
    #IO.inspect(lines)
    [h1,h2,h3|rest] = lines
    IO.inspect("h1:")
    IO.inspect(h1)
    IO.inspect("h2:")
    IO.inspect(h2)
    IO.inspect("h3:")
    IO.inspect(h3)
    part1 = MapSet.new(); part2 = MapSet.new(); part3 = MapSet.new();
    part1 = MapSet.new(String.graphemes(h1))
    part2 = MapSet.new(String.graphemes(h2))
    part3 = MapSet.new(String.graphemes(h3))
    IO.inspect("PART 1:")
    IO.inspect(part1)
    IO.inspect("PART 2:")
    IO.inspect(part2)
    IO.inspect("PART 3:")
    IO.inspect(part3)
    intersection = MapSet.intersection(part1,part2)
    IO.inspect("INTERSECTION 1:")
    IO.inspect(intersection)
    intersection = MapSet.to_list(MapSet.intersection(intersection,part3))
    IO.inspect("INTERSECTION 2:")
    IO.inspect(intersection)
    priorityFromIntersection(intersection)
  end

  def charUpperCaseChecker(value) do
    cond do
      (value - 64) <= 26 and (value - 64) >= 1 -> true
      (value - 96) <= 26 and (value - 96) >= 1 -> false
    end
  end
end

##################################
  # WILLIAM'S CODE FOR DAY3 PART 2 #
  ##################################
  # def loop_rows([], score) do score end
  # def loop_rows([first, second, third|rest], score) do
  #     set1 = String.to_charlist(first) |> MapSet.new()
  #     set2 = String.to_charlist(second) |> MapSet.new()
  #     set3 = String.to_charlist(third) |> MapSet.new()
  #     intersection = MapSet.intersection(set1, set2)
  #     intersection = MapSet.intersection(intersection, set3)
  #     [letter] = MapSet.to_list(intersection)
  #     value = get_priority_of_character(letter)
  #     loop_rows(rest, score + value)
  # end

  # def get_priority_of_character(letter) do
  #     cond do
  #         97 <= letter and letter <= 122 -> # is a-z
  #             letter - 96
  #         65 <= letter and letter <= 90 -> # is A-Z
  #             letter - 38
  #     end
  # end
