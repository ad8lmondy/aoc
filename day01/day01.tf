data "local_file" "input" {
  filename = "input.txt"
}

data "local_file" "test_input" {
  filename = "test_input.txt"
}

locals {
  input = data.local_file.input.content # choose which input you want here

  per_elf = split("\n\n", local.input)
  per_cal = [for e in local.per_elf :
    [for c in split("\n", e) : tonumber(trimspace(c))]
  ]
  # The Terraform 'sort' function only works on strings, so numbers are cast to string with leading zeros, sorted, then
  # cast back to number, lol
  sorted_per_elf_total = [for v in reverse(sort(formatlist("%09d", [ # 
    for t in local.per_cal : sum(t)]                                 # Sum each elf calorie load
    ))) : tonumber(v)                                                # Sorting: convert back to number
  ]
}

output "top_elf_cals" {
  value = local.sorted_per_elf_total[0]
}
output "top_3_elf_total_cals" {
  value = sum(slice(local.sorted_per_elf_total, 0, 3))
}