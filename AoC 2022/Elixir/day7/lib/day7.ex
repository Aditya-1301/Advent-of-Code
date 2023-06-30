defmodule Day7 do
  def readFile do
    input = File.read!("D:\\Advent_Of_Code\\AoC 2022\\Elixir\\day7\\lib\\input7.txt")
    |> String.split("\r\n")
    dirTree(input, 0)
  end

  def dirTree([input1|inputs], fileSize)do
    
  end
end
