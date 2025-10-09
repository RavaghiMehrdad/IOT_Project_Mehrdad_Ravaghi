'''




'''

class Device:
    
    def __init__(self,location,group,device_type,device_name):
        self.location=location
        self.group=group
        self.device_type=device_type
        self.device_name=device_name 
        self.status='off'


    def turn_on(self):
        print('Done!!!')
        self.status='on'
        #--_.code ejra mishe

    def turn_off(self):
        print('off')
        self.status='off'
        #code ejra mishe 
       
        
    def get_status(self):
        if self.status=='on':
            return True
        else:
            return False
        
        
        

class Sensor:
    
    def __init__(self,location,group,sensor_type,sensor_name):
        self.location=location
        self.group=group
        self.sensor_name=sensor_name
        self.sensor_type=sensor_type
                
        
    def read_data(self):
        return 25




class control_panel:
    
    def __init__(self):
        self.groups={}
        
    def create_group(self,group_name):
        if group_name not in self.groups:
            self.groups[group_name]=[]
            print(f'groups {group_name} created !!')
            
        else:
            print('your group name is duplicated')
        
    
    def add_device_to_group(self,group_name,device):
        if group_name in self.groups:
            self.groups[group_name].append(device)
            # groups['living_room'] -->[]
            print(f'your device is added to {group_name}')
        else:
            print('your group is not exist....')
        
        
        
        
    def create_device(self,group_name,device_type,device_name):
        
        if group_name in self.groups:
            location='home'
            new_device=Device(location,group_name,device_type,device_name)
            
            self.groups[group_name].append(new_device)
            print(f'{new_device} added successfully')
            
        else:
            print(f'{group_name} is not exist.')
        
        
        
        
    def create_multiple_device(self,group_name,device_type,device_number):
        if group_name in self.groups:
            
            for i in range(1,device_number+1):
                dv_name=f'{device_type}_{i}'
                self.create_device(group_name,device_type,dv_name)

            print(f'{device_number} devices created!!')
            
        else:
            
            print(f'{group_name} is not exist.')
            
            
            
    def get_devices(self,group_name):
        
        devices=self.groups[group_name]
        return devices
        
        
        
    def turn_on_in_group(self,group_name):
        
        if group_name in self.groups:
            
            devices=self.get_devices(group_name)
            
            for device in devices:
                device.turn_on()
            
        else:
            print(f'{group_name} is not exist.') 
            
            
            
    def turn_off_in_group(self,group_name):
        if group_name in self.groups:
            devices=self.get_devices(group_name)
            for device in devices:
                device.turn_off()
            
        else:
            print(f'{group_name} is not exist.') 
    
    
    def turn_on_all(self):
      for devices in self.groups.values():
        for device in devices:
            device.turn_on()
           
    
    def turn_off_all(self):
      for devices in self.groups.values():
        for device in devices:
            device.turn_off()
 
    
    def get_status_in_group(self,group_name):
        if group_name in self.groups:
            devices=self.get_devices(group_name)
            for device in devices:
                device.get_status()
                
        else:
            print(f'{group_name} is not exist.')  
        

        
    def get_status_in_device_type(self, device_type):
        
        for group_name, devices in self.groups.items():
            for device in devices:
                if device.device_type == device_type:
                    status = device.get_status()
                    print(f'status of {device_type} is {status}')
                    
        else:
            print(f'{device_type} is not exist.')

    
    def create_sensor(self,group_name,sensor_type,sensor_name):
            
            if group_name in self.groups:
                location='home'
                new_sensor=Sensor(location,group_name,sensor_type,sensor_name)
                
                self.groups[group_name].append(new_sensor)
                print(f'{new_sensor} added successfully')
                
            else:
                print(f'{group_name} is not exist.')    
        
    
    def create_multiple_sensor(self,group_name,sensor_type,sensor_number):
        if group_name in self.groups:  
            for i in range(1,sensor_number+1):
                sen_name=f'{sensor_type}_{i}'
                self.create_sensor(group_name,sensor_type,sen_name)

            print(f'{sensor_number} sensors created!!')
                
        else:
                
            print(f'{group_name} is not exist.')    
        
    
    
