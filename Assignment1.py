class Vehicle:
    vehicle_type = 'Car'
    def __init__(self, arr):
        self.vehicle_id = arr[0]
        self.make = arr[1]
        self.model = arr[2]
        self.year = arr[3]
        self.rental_rate = arr[4]
        self.availability = arr[5]
    
    def display(self):
        print('Unique Vehicle ID:', self.vehicle_id)
        print('{} {}'.format(self.make,self.model))
        print('Year of Manufacture:', self.year)
        print('Rental rate:', self.rental_rate)
        print()
    
    def rent(self, customer_id, rental_duration):
        if self.availability:
            print('{} {} rented succesfully by customer {} for {} days!'.format(self.make, self.model, customer_id, rental_duration))
            self.availability = False
            
        else:
            print('{} {} is not available right now. Would you be interested in other options?'.format(self.make, self.model))
        
    def unrent(self):
        self.availability = True

class LuxuryVehicle(Vehicle):
    lux_premium = 1.2
    def __init__(self, arr, extra_features = None):
        super().__init__(arr)
        self.rental_rate *= self.lux_premium
        self.extra_features = [] if extra_features is None else extra_features

    def luxPrice(self):
        price = self.rental_rate
        for f in self.extra_features:
            if f == 'Leather seats':
                price+= self.rental_rate*0.05
            elif f == 'GPS':
                price+= 5000
            elif f == 'Tinted windows':
                price+= 2500
            elif f == 'No brakes':
                price = price
            elif f == 'Machine gun':
                price+= 10000
            elif f == 'Turns into a boat':
                price+= 90000
            elif f == 'A massive picture of Tom Cruise on the windshield':
                price+= 25000
            elif f == 'Aura':
                price += 1000000
        return price

    @staticmethod
    def mapFeat(featno):
        if featno == '1':
            return 'Leather seats'
        elif featno == '2':
            return 'GPS'
        elif featno == '3':
            return 'Tinted windows'
        elif featno == '4':
            return 'No brakes'
        elif featno == '5':
            return 'Machine gun'
        elif featno == '6':
            return 'Turns into a boat'
        elif featno == '7':
            return 'A massive picture of Tom Cruise on the windshield'
        elif featno == '8':
            return 'Aura'
        else:
            return None
    
    def display(self):
        super().display()

class RentalManager:
    total_vehicles = [['V000001', 'Toyota', 'Corolla', 2025, 25000,True], ['V000002', 'Subaru', 'Outback', 2015, 100000, True], ['V000003', 'MG','Hector', 2006 , 50000, True], ['V000004', 'Lamborghini', 'Aventador', 2024, 75000, True], ['V000005', 'Tata', 'Nexon', 2015, 12500, True]]
    available_vehicles = total_vehicles
    rented_vehicles = []    
    all_customers = []
    rent_list = []
    sales = 0

    @staticmethod
    def updateListRent():
        RentalManager.available_vehicles = list(filter(lambda a: a[5], RentalManager.total_vehicles))
        RentalManager.rented_vehicles = list(filter(lambda a: not a[5], RentalManager.total_vehicles))
    
    @staticmethod
    def updateList(vobj):
        for entry in RentalManager.total_vehicles:
            if vobj.vehicle_id == entry[0]:
                entry[5] = vobj.availability

class Customer:
    def __init__(self, arr, rental_history = None, loyalty = 0, premium = False):
        self.customer_id = arr[0]
        self.name = arr[1]
        self.contact_info = arr[2]
        self.rental_history = [] if rental_history is None else rental_history
        self.loyalty_amt = loyalty
        self.premium = premium

    @staticmethod
    def regCustomer():
        print('Kindly register as a customer using your name and mobile number')
        name = input('Enter name: ')
        mob = input('Enter mobile number: ')
        loy = 0

        l = len(RentalManager.all_customers)
        if l<10:
            cid = 'C00' + str(l)
        elif l<100:
            cid = 'C0' + str(l)
        else:
            cid = 'C' + str(l)

        cust_arr = [cid, name, mob, loy]
        cobj = Customer(cust_arr)
        RentalManager.all_customers.append(cobj)
        print('Congratulations! You have been registered as a customer')
        print()
        return cobj
    
    @staticmethod
    def welcOldCustomer():
        cid = input(print('Welcome back brotha! Kindly enter your customer id: '))
        flag = 0
        for cust in RentalManager.all_customers:
            if cid == cust.customer_id:
                flag = 1
                print('Your customer details are as follows:')
                cust.display()
                return cust
        if flag == 0:
            return False
    
    def addLoyalty(self, rental_rate):
        self.loyalty_amt += (rental_rate * 0.01)
    
    def updateRentHistory(self, entry):
        self.rental_history.append(entry)

    def showRentHistory(self):
        print('List of rented Vehicles:')
        for vehicle in self.rental_history:
            print('{} {} rented for {} days'.format(vehicle[0], vehicle[1], vehicle[2]))
    
    def display(self):
        print('Unique Customer ID:', self.customer_id)
        print('Name: ', self.name)
        print('Contact info:', self.contact_info)
        print('Loyalty points:', self.loyalty_amt)
        print()

class PremiumCustomer(Customer):
    disc_per = 0.9
    
    def __innit__(self, arr):
        super().__init__(arr)
        self.premium = True

    def premDiscount(self, rental_rate):
        return rental_rate * self.disc_per

robj = RentalManager()

while True is True:
    #Intro message
    print('Hello! Are you a customer (press C) or a manager (press M)')
    c1 = input() #Choice of the user
    if c1=='c' or c1=='C':

        #CHOICE- User is a customer
        print('Welcome to Mangalyaan Car Rental Service! Do you want to rent (press A) or return (press B)')
        c2 = input()

        if c2=='a' or c2=='A':
            #CHOICE- User wants to rent a vehicle
            print('Are you a new customer (press N) or an existing customer (press E)')
            c3 = input()
            if c3=='n' or c3=='N':
                #Registering a new customer with a customer ID
                cobj = Customer.regCustomer()
            
            if c3=='e' or c3=='E':
                #Welcoming previously registered customers
                cobj = Customer.welcOldCustomer()
                if cobj.premium:
                    print('On account of being a premium customer, enjoy a 10 percent discount!')
                    cobj = PremiumCustomer([cobj.customer_id, cobj.name, cobj.contact_info])
                    cobj.premium = True
                if not cobj:
                    print('It seems we do not have you in our records. Please try again')
                    continue
                        
            #Displaying vehicle collection to prospective buyer
            print('Here are the vehicles we have right now')
            for v in RentalManager.available_vehicles:
                vobj = Vehicle(v)
                vobj.display()

            #Taking rental info from the buyer
            vid = input('Enter vehicle id of vehicle you wanna rent-')
            dur = int(input('Enter the number of days you wanna rent for-'))

            rented = [] #Stores details of rented vehicle
            for vehicle in RentalManager.available_vehicles: 
                if vid == vehicle[0]: #Finding the selected vehicle among the available vehicles
                    rented = vehicle
                    vobj = Vehicle(vehicle)
                    vobj.rent(cobj.customer_id, dur) #Changing the vehicle's availability to false
                    vehicle[5] = vobj.availability
                    robj.updateListRent() #Updating the record to reflect change in vehicle availability
                    break

            rent_price = 0 #Variable to store the price of this particular transaction
            vrent = None #Will eventually become a vehicle object

            #Giving buyer the choice of luxury features
            print('Would you like any luxury features to go along with your vehicle?')
            print('1. Leather Seats: +5 percent of price')
            print('2. GPS: +5000')
            print('3. Tinted Windows: +2500')
            print('4. No brakes: Free')
            print('5. Machine gun: +10000')
            print('6. Turns into a boat +90000')
            print()
            if cobj.premium:
                print('Premium only features:')
                print('7. A massive picture of Tom Cruise on the windshield: +25000')
                print('8. Aura: +1000000')
            print('Additional 20% premium on base price for luxury features')
            print('All cost values in terms of rental rate per day')
            print('Type y if you want to select luxury features, else type any other character')
            c4 = input() #Initial choice of the customer
            feats = [] #Stores the serial numbers of selected features

            #CHOICE- Luxury Features yes (maybe)
            if c4 == 'y':
                print('Type the number for the feature you want, and press enter afterwards. Once you are done choosing, press n and enter')
                print()
                while c4 != 'n':
                    c4 = input()
                    if cobj.premium:
                        if c4 not in ['1', '2', '3', '4', '5', '6', '7', '8', 'n']:
                            print('Invalid input. Valid inputs--> 1, 2, 3, 4, 5, 6, 7, 8 or n')
                            continue
                        feats.append(c4)
                    else: 
                        if c4 not in ['1', '2', '3', '4', '5', '6', 'n']:
                            print('Invalid input. Valid inputs--> 1, 2, 3, 4, 5, 6 or n')
                            continue
                        feats.append(c4)
                feats = list(map(LuxuryVehicle.mapFeat, feats)) #Mapping the serial numbers with the feature names
                vrent = LuxuryVehicle(rented,feats) #Initialising our vehicle object as a luxury vehicle
                rent_price = dur * vrent.luxPrice() #Total rent price- special function for calculating price of luxury additions

            #CHOICE- No Luxury Features
            else:
                vrent = Vehicle(rented) #Initialising our vehicle object as a regular vehicle
                rent_price = dur * vrent.rental_rate #Total rent price

            #Customer rent history updated
            entry = [vrent.make, vrent.model, dur] 
            cobj.updateRentHistory(entry)

            #Applying premium discount
            if cobj.premium:
                rent_price = cobj.premDiscount(rent_price)

            #Updating total sales
            RentalManager.sales += rent_price

            #Checkout 
            print('Proceeding to checkout...')
            print('Congratulations on your purchase! Your purchase details are as follows-')
            print()
            print('Total cost:', rent_price)
            print()
            print('Customer id: ', cobj.customer_id)
            print('{} {} rented for {} days'.format(entry[0], entry[1], entry[2]))
            print('Remember your customer ID, as it is important for returning rented vehicles, redeeming loyalty points, and more')
            print('Happy driving!')
            print()

            returned = False
            RentalManager.rent_list.append([cobj.customer_id, vrent, rent_price, dur, returned]) #Updating store's rent history
            cobj.addLoyalty(rent_price) #Updating customer's loyalty points
        
        elif c2=='b' or c2=='B':
            #CHOICE- User wants to return a vehicle
            cid = input(('Enter your customer ID: '))

            #Looking for our customer id in the most recent iterations of the rental list 
            for rent in reversed(RentalManager.rent_list):
                if rent[0] == cid:
                    #Making sure the vehicle is currently rented out
                    if not rent[4]:
                        rent[1].unrent()
                        print('Thank you for returning your {} {}'.format(rent[1].make, rent[1].model))
                        print()
                        print('Loyalty points added to your account!')
                        for cust in RentalManager.all_customers:
                            if cust.customer_id == cid:
                                loyalty = cust.loyalty_amt
                                if loyalty > 10000 and not cust.premium:
                                    cust.premium = True
                                    print('Congratulations! You have been upgraded to a Premium Customer!')
                                    print('Enjoy a 10 percent discount on all future rentals, as well as additional special features')
                                elif loyalty < 10000:
                                    print('Only {} points away from upgrading to a premium customer!'.format(10000 - loyalty))
                        print()
                        print('Hope to do business with you again!')
                        robj.updateList(rent[1]) #Updating availability of our vehicle in the list of vehicles
                        robj.updateListRent() #Updating list of rented and available vehicles
                        rent[4] = True 
                    else:
                        print('No vehicles owed for rent. You may leave')
                    break

    elif c1=='m' or c1=='M':
        #CHOICE- User is a manager
        while True is True:
            print('Press the required key for what you want to access. To exit, press any other key')
            print('a --> View available vehicles')
            print('b --> View rented vehicles')
            print('c --> View list of customers')
            print('d --> View customer rental history')
            print('e --> Add new vehicle')
            print('f --> View total sales')
            c2 = input() #Input to decide manager task
            if c2 == 'a': #Displaying available vehicles
                for v in RentalManager.available_vehicles:
                    vobj = Vehicle(v)
                    vobj.display()
            elif c2 == 'b': #Displaying rented vehicles
                flag = 0
                for v in RentalManager.rent_list:
                    if not v[4]:
                        print('Customer id:', v[0])
                        print(v[1].display())
                        print('Total rental price:', v[2])
                        print('Duration: {} days'.format(v[3]))
                        print()
                        flag = 1
                if flag == 0:
                    print('No vehicles currently rented')
            elif c2 == 'c': #Displaying all customers
                for c in RentalManager.all_customers:
                    c.display()
            elif c2 == 'd': #Showing rental history of a particular customer
                print('Enter customer ID')
                cid = input()
                for c in RentalManager.all_customers:
                    if c.customer_id == cid:
                        c.showRentHistory()
                        break
            elif c2 == 'e': #Creating new vehicle object
                l = len(RentalManager.total_vehicles) + 1
                if l<10:
                    vid = 'V00000' + str(l)
                elif l<100:
                    vid = 'V0000' + str(l)
                elif l<1000:
                    vid = 'V000' + str(l)
                elif l<10000:
                    vid = 'V00' + str(l)
                elif l<100000:
                    vid = 'V0' + str(l)
                else:
                    vid = 'V' + str(l)
                print('Enter make')
                make = input()
                print('Enter model')
                model = input()
                print('Enter year of manufacture')
                year = input()
                print('Enter rental rate')
                rental_rate = input()
                arr = [vid, make, model, year, rental_rate, True]
                RentalManager.total_vehicles.append(arr)
                print('Vehicle succesfully added')
                print()
                vobj = Vehicle(arr)
                print('Vehicle details: ')
                vobj.display()
            elif c2 == 'f': #Displaying Total Sales
                print('Total sales:', RentalManager.sales)
            else:
                break
                   
                
    if c1=='Secret code':
        break




