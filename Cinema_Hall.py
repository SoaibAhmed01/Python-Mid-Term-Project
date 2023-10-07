class Star_cinema:
    hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.hall_list.append(hall)


class Hall:
    def __init__(self, row, col, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__row = row
        self.__col = col
        self.__hall_no = hall_no
        self.__empty_seats()

        Star_cinema.entry_hall(self)

    def get_show_list(self):
        return self.__show_list

    def __empty_seats(self):
        for rows in range(1, self.__row + 1):
            self.__seats[rows] = [0] * self.__col

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.__show_list.append(show_info)
        seats = [[0 for _ in range(self.__col)] for _ in range(self.__row)]
        self.__seats[id] = seats

    def book_seats(self, id, seat_list):
        if id not in self.__seats:
            print(f"Wrong Id {id}")
            return
        seats = self.__seats[id]
        for row, col in seat_list:
            if 1 <= row <= self.__row and 1 <= col <= self.__col and seats[row - 1][col - 1] != 1:
                seats[row - 1][col - 1] = 1
            else:
                print(f"Error: Wrong seat ({row}, {col}) for show {id}")

    def view_show_list(self):
        print("Shows Ongoing:")
        for show in self.__show_list:
            show_id, movie_name, time = show
            print(f"Movie Name: {movie_name} (Show ID: {show_id}) Time: {time}")

    def view_available_seats(self, id):
        if id not in self.__seats:
            print(f"Your id {id} is wrong")
            return
        seats = self.__seats[id]
        print(f"Available Seats for show {id}: ")
        for row in seats:
            row_str = " ".join(str(seat) for seat in row)
            print(row_str)

        for show in self.get_show_list():
            show_id, _, _ = show
            if show_id == id:
                print(f"Movie Name: {show[1]} (Show ID: {show_id}) Time: {show[2]}")
                break
        else:
            print(f"Wrong Show ID {id}")


hall1 = Hall(10, 10, 111)
hall2 = Hall(10, 10, 125)

hall1.entry_show(111, "Jawan", "7/10/2023 11:00 AM")
hall1.entry_show(125, "Pathan", "7/10/2023 2:00 PM")
hall1.entry_show(128, "Pera Nai Chill", "7/10/2023 2:00 PM")
hall1.entry_show(225, "Mone Eto Kosto Kno!", "7/10/2023 2:00 PM")

while True:
    print("Welcome to Our Cinema Hall\n")
    print("1. View All Show Today")
    print("2. View Available Seats")
    print("3. Book Ticket")
    print("4. Exit")

    op = int(input("Enter Option: "))

    if op == 1:
        for hall in Star_cinema.hall_list:
            hall.view_show_list()

    elif op == 2:
        show_id = int(input("Enter Show ID: "))
        flag = False
        for hall in Star_cinema.hall_list:
            if show_id in [show[0] for show in hall.get_show_list()]:
                hall.view_available_seats(show_id)
                flag = True
                break
        if not flag:
            print(f"Wrong Show ID {show_id}")

    elif op == 3:
        show_id = int(input("Enter Show ID: "))
        flag = False
        for hall in Star_cinema.hall_list:
            for show in hall.get_show_list():
                if show_id == show[0]:
                    num_tickets = int(input("Number of Tickets?: "))
                    if num_tickets <= 0:
                        print("Invalid tickets.")
                        flag = True
                        break
                    seat_list = []
                    for _ in range(num_tickets):
                        seat_row = int(input(f"Enter Seat Row: "))
                        seat_col = int(input(f"Enter Seat Col: "))
                        seat_list.append((seat_row, seat_col))
                    hall.book_seats(show_id, seat_list)
                    flag = True
                    for seat_row, seat_col in seat_list:
                        print(f"Seat ({seat_row}, {seat_col}) booked for show {show_id}")
                    break
            if flag:
                break
        if not flag:
            print(f"Wrong Show ID {show_id}")

    if op == 4:
        print("Thank you for coming to our Cinema Hall. Sayonara!")
        break