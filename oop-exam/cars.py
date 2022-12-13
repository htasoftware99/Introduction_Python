from abc import ABC,abstractmethod

class Cars(ABC):
    def __init__(self,model,color,weight,year,country,current_speed,current_fuel,fuel_type,brake_type,price,register_no):
        #Tüm arabalarda olan ortak özellikler
        self.model = model
        self.color = color
        self.weight = weight
        self.year = year
        self.country = country
        self.current_speed = current_speed
        self.current_fuel = current_fuel
        self.fuel_type = fuel_type
        self.brake_type = brake_type
        self._price = price
        self.__register_no = register_no
        
    
    #Tüm arabalarda olan ortak methodlar
    @abstractmethod
    def no_of_tires(self):
        pass
    
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def max_speed(self):
        pass

    def speed_up(self):
        if self.current_speed >= 120:
            print("You can't speed up anymore")
        else:
            self.current_speed += 5
    
    def speed_down(self):
        if self.current_speed == 0:
            print("You are already at 0 speed")
        else:
            self.current_speed -= 5
    
    def stop(self):
        return self.current_speed == 0  

    def show_speed(self):
        return self.current_speed

    def add_fuel(self,x):
        self.current_fuel += x 
    
    def show_fuel(self):
        return self.current_fuel
    
    def show(self):
        return f"Model : {self.model} \nColor : {self.color} \nWeight : {self.weight} kilograms \nYear : {self.year} \nCountry : {self.country} \nCurrent Speed : {self.current_speed} km/h \nCurrent Fuel : {self.current_fuel} Liter(s) \nFuel Type: {self.fuel_type} \nBrake Type : {self.brake_type} \nPrice : {self._price} Dollars \nRegister No : {self.__register_no}"

    def type_of_fuel(self):
        return f"{self.model} uses {self.fuel_type} as fuel."

    def type_of_brake(self):
        return f"{self.model} uses {self.brake_type} as brake"
    

class BMW(Cars):
    def __init__(self,color,weight,year,country,current_speed,current_fuel,fuel_type,brake_type,price,register_no,model,sunroof_status="OFF"):
        Cars.__init__(self,color,weight,year,country,current_speed,current_fuel,fuel_type,brake_type,price,register_no,model)
        #Sadece BMW classında olan bir özellik ekledim
        self.sunroof_status = sunroof_status

    #Cars classındaki no_of_tires methodunu override ediyoruz abstractla
    def no_of_tires(self):
        return f"{self.model} has 4 tires."
    
    # Bu da Abstract ediliyor
    def start(self):
        return f"{self.model} has started its engines."
    
    #Bu da abstract ediliyor
    def max_speed(self):
        return f"BMW models' max speed is 350km/h"

    #Sadece BMW classı içinde kullanabileceğimz bir method
    def open_sunroof(self):
        if self.sunroof_status == "OFF":
            self.sunroof_status = "ON"
        
        else:
            print("Sunroof is already open.")

    def close_sunroof(self):
        if self.sunroof_status == "ON":
            self.sunroof_status = "OFF"
        
        else:
            print("Sunroof is already closed.")

    def show_sunroof_status(self):
        return self.sunroof_status
    

class Tesla(Cars):
    def __init__(self,color,weight,year,country,current_speed,current_fuel,fuel_type,brake_type,price,register_no,model,autopilot_mode = "OFF"):
        Cars.__init__(self,color,weight,year,country,current_speed,current_fuel,fuel_type,brake_type,price,register_no,model)
        #Sadece Teslalarda olan bir özellik ekledim
        self.autopilot_mode = autopilot_mode

    #Cars classındaki no_of_tires methodunu override ediyoruz abstractla
    def no_of_tires(self):
        return f"{self.model} has 4 tires."
    
    # Bu da Abstract ediliyor
    def start(self):
        return f"{self.model} has started its engines."
    
    #Bu da abstract ediliyor
    def max_speed(self):
        return f"Tesla models' max speed is 300km/h"

    #Sadece Tesla classı içinde kullanabileceğimz bir method
    def open_autopilot(self):
        if self.autopilot_mode == "OFF":
            self.autopilot_mode = "ON"
        
        else:
            print("Autopilot is already open.")

    def close_autopilot(self):
        if self.autopilot_mode == "ON":
            self.autopilot_mode = "OFF"
        
        else:
            print("Autopilot is already disabled.")

    def show_autopilot_mode(self):
        return self.autopilot_mode

bmw1 = BMW("X8","Black",500,2000,"Germany",30,26,"Diesel","Hydraulic",100000,200444004)
print(bmw1.show_speed())
bmw1.speed_up()
print(bmw1.show_speed())
bmw1.close_sunroof()