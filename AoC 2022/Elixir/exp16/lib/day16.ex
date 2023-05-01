defmodule D16 do

  # Answer part 1 -> 1880
  # Answer part 2 -> 2520

  def read() do
    {:ok, input} = File.read("input16.txt")
    rows = input |> String.split("\n")
    rows = Enum.map(rows, fn row ->
      String.split(row, ["Valve ", " has flow rate=", "; tunnels lead to valves ",  "; tunnel leads to valve ", ", "], trim: true) end)
    rows = Enum.map(rows, fn row ->
      [src, rate | valves] = row; res = {src, String.to_integer(rate),  Enum.map(valves, fn el ->
        String.trim(el, "\r")end)}; res end)
    g = List.foldl(rows,Map.new(),fn row,acc -> Map.put(acc,elem(row,0),%{flow: elem(row,1), nbrs: elem(row,2)}) end)
    g
  end

  def djk(_, [], visited) do

  end

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
  end

end
