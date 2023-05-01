defmodule D16_1 do

  def graph() do
    graph = %{
      "VR" => %{flow_rate: 11, edges: ["LH", "KV", "BP"]},
      "UV" => %{flow_rate: 0, edges: ["GH", "RO"]},
      "OH" => %{flow_rate: 0, edges: ["AJ", "NY"]},
      "GD" => %{flow_rate: 0, edges: ["TX", "PW"]},
      "NS" => %{flow_rate: 0, edges: ["AJ", "AA"]},
      "KZ" => %{flow_rate: 18, edges: ["KO", "VK", "PJ"]},
      "AH" => %{flow_rate: 0, edges: ["ZP", "DI"]},
      "SA" => %{flow_rate: 0, edges: ["VG", "JF"]},
      "VK" => %{flow_rate: 0, edges: ["RO", "KZ"]},
      "GB" => %{flow_rate: 0, edges: ["XH", "AA"]},
      "AJ" => %{flow_rate: 6, edges: ["IC", "OH", "ZR", "NS", "EM"]},
      "PJ" => %{flow_rate: 0, edges: ["KZ", "SP"]},
      "KO" => %{flow_rate: 0, edges: ["KZ", "LE"]},
      "AA" => %{flow_rate: 0, edges: ["TW", "GB", "TI", "NS", "UL"]},
      "TW" => %{flow_rate: 0, edges: ["TU", "AA"]},
      "VG" => %{flow_rate: 25, edges: ["SA"]},
      "BP" => %{flow_rate: 0, edges: ["RO", "VR"]},
      "XH" => %{flow_rate: 0, edges: ["GB", "RI"]},
      "TX" => %{flow_rate: 0, edges: ["RI", "GD"]},
      "IR" => %{flow_rate: 10, edges: ["TN", "NY", "JF"]},
      "TU" => %{flow_rate: 0, edges: ["JD", "TW"]},
      "KC" => %{flow_rate: 0, edges: ["SP", "RO"]},
      "LN" => %{flow_rate: 0, edges: ["EM", "RI"]},
      "HD" => %{flow_rate: 0, edges: ["FE", "SC"]},
      "KE" => %{flow_rate: 0, edges: ["OM", "RI"]},
      "VY" => %{flow_rate: 0, edges: ["PW", "BS"]},
      "LH" => %{flow_rate: 0, edges: ["OM", "VR"]},
      "EM" => %{flow_rate: 0, edges: ["AJ", "LN"]},
      "SO" => %{flow_rate: 22, edges: ["ZP", "FE"]},
      "EC" => %{flow_rate: 0, edges: ["OM", "UL"]},
      "KV" => %{flow_rate: 0, edges: ["SP", "VR"]},
      "FE" => %{flow_rate: 0, edges: ["SO", "HD"]},
      "TI" => %{flow_rate: 0, edges: ["AA", "PW"]},
      "SC" => %{flow_rate: 14, edges: ["HD"]},
      "ZP" => %{flow_rate: 0, edges: ["SO", "AH"]},
      "RO" => %{flow_rate: 19, edges: ["UV", "BP", "VK", "KC"]},
      "ZR" => %{flow_rate: 0, edges: ["OM", "AJ"]},
      "JL" => %{flow_rate: 21, edges: ["GN", "TN"]},
      "PW" => %{flow_rate: 9, edges: ["TI", "GN", "VY", "GD", "IC"]},
      "UL" => %{flow_rate: 0, edges: ["EC", "AA"]},
      "GN" => %{flow_rate: 0, edges: ["JL", "PW"]},
      "TN" => %{flow_rate: 0, edges: ["JL", "IR"]},
      "NV" => %{flow_rate: 0, edges: ["RI", "JD"]},
      "DI" => %{flow_rate: 23, edges: ["LE", "AH"]},
      "IC" => %{flow_rate: 0, edges: ["PW", "AJ"]},
      "JF" => %{flow_rate: 0, edges: ["SA", "IR"]},
      "LE" => %{flow_rate: 0, edges: ["DI", "KO"]},
      "BS" => %{flow_rate: 0, edges: ["JD", "VY"]},
      "JD" => %{flow_rate: 15, edges: ["NV", "TU", "BS"]},
      "SP" => %{flow_rate: 24, edges: ["KC", "KV", "PJ"]},
      "NY" => %{flow_rate: 0, edges: ["IR", "OH"]},
      "OM" => %{flow_rate: 7, edges: ["EC", "GH", "KE", "ZR", "LH"]},
      "GH" => %{flow_rate: 0, edges: ["OM", "UV"]},
      "RI" => %{flow_rate: 3, edges: ["NV", "KE", "LN", "XH", "TX"]}
    }
    Map.to_list(graph)
  end

  def list() do
    list = [
      {"VR", 11, ["LH", "KV", "BP"]},
      {"UV", 0, ["GH", "RO"]},
      {"OH", 0, ["AJ", "NY"]},
      {"GD", 0, ["TX", "PW"]},
      {"NS", 0, ["AJ", "AA"]},
      {"KZ", 18, ["KO", "VK", "PJ"]},
      {"AH", 0, ["ZP", "DI"]},
      {"SA", 0, ["VG", "JF"]},
      {"VK", 0, ["RO", "KZ"]},
      {"GB", 0, ["XH", "AA"]},
      {"AJ", 6, ["IC", "OH", "ZR", "NS", "EM"]},
      {"PJ", 0, ["KZ", "SP"]},
      {"KO", 0, ["KZ", "LE"]},
      {"AA", 0, ["TW", "GB", "TI", "NS", "UL"]},
      {"TW", 0, ["TU", "AA"]},
      {"VG", 25, ["SA"]},
      {"BP", 0, ["RO", "VR"]},
      {"XH", 0, ["GB", "RI"]},
      {"TX", 0, ["RI", "GD"]},
      {"IR", 10, ["TN", "NY", "JF"]},
      {"TU", 0, ["JD", "TW"]},
      {"KC", 0, ["SP", "RO"]},
      {"LN", 0, ["EM", "RI"]},
      {"HD", 0, ["FE", "SC"]},
      {"KE", 0, ["OM", "RI"]},
      {"VY", 0, ["PW", "BS"]},
      {"LH", 0, ["OM", "VR"]},
      {"EM", 0, ["AJ", "LN"]},
      {"SO", 22, ["ZP", "FE"]},
      {"EC", 0, ["OM", "UL"]},
      {"KV", 0, ["SP", "VR"]},
      {"FE", 0, ["SO", "HD"]},
      {"TI", 0, ["AA", "PW"]},
      {"SC", 14, ["HD"]},
      {"ZP", 0, ["SO", "AH"]},
      {"RO", 19, ["UV", "BP", "VK", "KC"]},
      {"ZR", 0, ["OM", "AJ"]},
      {"JL", 21, ["GN", "TN"]},
      {"PW", 9, ["TI", "GN", "VY", "GD", "IC"]},
      {"UL", 0, ["EC", "AA"]},
      {"GN", 0, ["JL", "PW"]},
      {"TN", 0, ["JL", "IR"]},
      {"NV", 0, ["RI", "JD"]},
      {"DI", 23, ["LE", "AH"]},
      {"IC", 0, ["PW", "AJ"]},
      {"JF", 0, ["SA", "IR"]},
      {"LE", 0, ["DI", "KO"]},
      {"BS", 0, ["JD", "VY"]},
      {"JD", 15, ["NV", "TU", "BS"]},
      {"SP", 24, ["KC", "KV", "PJ"]},
      {"NY", 0, ["IR", "OH"]},
      {"OM", 7, ["EC", "GH", "KE", "ZR", "LH"]},
      {"GH", 0, ["OM", "UV"]},
      {"RI", 3, ["NV", "KE", "LN", "XH", "TX"]}
    ]
  end

  def getUnvisitedNodes(graph) do
    list = Map.to_list(graph)
    Enum.filter(list, fn({node, map}) -> {:ok, val} = Map.fetch(map, :flow_rate); val > 0 end)
    |> Enum.map(fn({node, map}) -> node end)
  end

  # Floyd Warshall Algorithm needed for this part
  def findShortestPathBetweenNodes(_,_,_) do 0 end
  def findShortestPathBetweenNodes(nodeA, nodeB, graph) do

  end

  #Calculate score
  def calculateScore(node, graph, distance, timeLeft) do
    {:ok, map} = Map.fetch(graph, node)
    {:ok, flow_rate} = Map.fetch(map, :flow_rate)
    timeLeft = timeLeft - distance - 1
    cond do
      timeLeft < 0 -> :outoftime
      true ->
        score = timeLeft*flow_rate
        {score, timeLeft}
    end
  end

  #If we run out of time, we return -1
  def dfs(_, _, _, _, _) do -1 end

  def dfs(_, _, [], timeLeft, score) do
    cond do
      timeLeft < 0 -> -1
      true -> score
    end
  end

  def dfs(start, graph, unvisited, timeLeft, score) when timeLeft > 0 do
    for node <- unvisited do
      distance = findShortestPathBetweenNodes(start, node, graph)
      response = calculateScore(node, graph, distance, timeLeft)
      case response do
        :outoftime -> -1
        true -> {score, timeLeft} = response; dfs(node, graph, List.delete(unvisited, node), timeLeft, score)
      end
    end |> Enum.max
  end
end
