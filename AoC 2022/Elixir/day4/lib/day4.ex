defmodule Day4 do
  def readFile() do
    file = "input.txt"
    file_linux = "/mnt/d/Elixir/Advent_Of_Code/Elixir/day4/lib/input.txt"
    input = File.read!(file)
    s = String.split(input, [",", "\r\n"])
    IO.inspect(s)
    list = for s1 <- s do
       String.split(s1, "-")
    end
    IO.inspect("Part1: #{length(overlap(list, [], :part1))}")
    IO.inspect("Part2: #{length(overlap(list, [], :part2))}")
  end

  def overlap([], acc, _) do acc end
  def overlap([a,b|rest], acc, flag)do
    [a1, a2] = a
    {i1, ""} = Integer.parse(a1)
    {i2, ""} = Integer.parse(a2)
    [b1, b2] = b
    {i3, ""} = Integer.parse(b1)
    {i4, ""} = Integer.parse(b2)
    m1 = MapSet.new(i1..i2)
    m2 = MapSet.new(i3..i4)
    case flag do
      :part1 ->
        if MapSet.intersection(m1,m2) == m1 or MapSet.intersection(m1,m2) == m2 do
          overlap(rest, acc ++ [true], :part1)
        else
          overlap(rest, acc, :part1)
        end
      :part2 ->
        if MapSet.intersection(m1,m2) != %MapSet{} do
          overlap(rest, acc ++ [true], :part2)
        else
          overlap(rest, acc, :part2)
        end
    end
  end
end
