defmodule Day5 do
  def readFile() do
    stacks = [
      "PGRN",
      "CDGFLBTJ",
      "VSM",
      "PZCRSL",
      "QDWCVLSP",
      "SMDWNTC",
      "PWGDH",
      "VMCSHPLZ",
      "ZGWLFPR"
    ]
    input = File.read!("D:\\Elixir\\AdventOfCode2022inElixir\\day5\\lib\\input5.txt")
    |> String.split("\r\n")
    input2 = for i <- input do
      String.split(i, ["move ", " from ", " to "]) |> Enum.reject( fn x -> x == "" end )
    end
    IO.inspect(stacks)
    move_from_to(stacks, input2)
    # s1 = move_from_to(stacks, input2)
    # #IO.inspect(s1)
    # String.at(Enum.at(s1,0),0) <> String.at(Enum.at(s1,1),0) <> String.at(Enum.at(s1,2),0) <> String.at(Enum.at(s1,3),0) <> String.at(Enum.at(s1,4),0) <> String.at(Enum.at(s1,5),0) <> String.at(Enum.at(s1,6),0) <> String.at(Enum.at(s1,7),0) <> String.at(Enum.at(s1,8),0)
  end

  def move_from_to(stacks, []) do stacks end
  def move_from_to(stacks, [move | move_list])do
    [a,b,c] = move
    {a1, _} = Integer.parse(a)
    {b1, _} = Integer.parse(b)
    {c1, _} = Integer.parse(c)
    s_i = Enum.at(stacks, b1 - 1)
    s_i1 = Enum.at(stacks, c1 - 1)
    s_i2 = String.replace(s_i, String.slice(s_i, 0..(a1 - 1)), "")
    #IO.inspect(s_i2)
    s_i3 = String.reverse(String.slice(s_i, 0..(a1 - 1))) <> s_i1
    #IO.inspect(s_i3)
    stacks2 = List.replace_at(stacks, b1-1, s_i2)
    stacks2 = List.replace_at(stacks2, c1-1, s_i3)
    #IO.inspect({stacks2,move})
    move_from_to(stacks2, move_list)
  end
end
