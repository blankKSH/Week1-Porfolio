lab_group=24
first_sce=113
first_group=int(first_sce/24)
remain_first=(first_sce%24)
print("For a group of 113 students, there will be", first_group, "full groups while", remain_first, "students will be in the left over group")

second_sce=174
second_group=int(second_sce/24)
remain_second=(second_sce%24)
print("For a group of 174 students, there will be", second_group, "full groups while", remain_second, "students will be in the left over group")

third_sce=12
print("For a group of 12 students, there will be no full groups. Only one small group of 12 students")
