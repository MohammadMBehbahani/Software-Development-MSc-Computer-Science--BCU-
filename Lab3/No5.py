def percent(listof_ho, sum_house):
    my_list_percent = []
    for item in listof_ho:
        per = (item / sum_house) * 100
        my_list_percent.append(per)
    
    return my_list_percent


def no_ho():
    sum_num = 0
    my_list_ho = []
    for i in range(8):
        houses = int(input(f"Provide the number of houses with {i} occupancy: "))
        sum_num = sum_num + houses
        my_list_ho.append(houses)
        
    return my_list_ho, sum_num


def main():
    noHo_list, noHo_sum = no_ho()
    percent_list = percent(noHo_list, noHo_sum)
    
    print(" Occupants 0 1 2 3 4 5 6 >6 \n No. houses {} {} {} {} {} {} {} {} \n {:.1f} {:.1f} {:.1f} {:.1f} {:.1f} {:.1f} {:.1f} {:.1f}".format(noHo_list[0],
                                                                                                          noHo_list[1],
                                                                                                          noHo_list[2],
                                                                                                          noHo_list[3],
                                                                                                          noHo_list[4],
                                                                                                          noHo_list[5],
                                                                                                          noHo_list[6],
                                                                                                          noHo_list[7],
                                                                                                          percent_list[0],
                                                                                                          percent_list[1],
                                                                                                          percent_list[2],
                                                                                                          percent_list[3],
                                                                                                          percent_list[4],
                                                                                                          percent_list[5],
                                                                                                          percent_list[6],
                                                                                                          percent_list[7]))
    
    
main()

