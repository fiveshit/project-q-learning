import serial
import sys
import threading
from queue import Queue
class Rfcomm(object):
    def __init__(self):
        self.port0 = '/dev/rfcomm1'
        self.port1 = '/dev/rfcomm2'
        self.port2 = '/dev/rfcomm3'
        self.port3 = '/dev/rfcomm4'
        self.port4 = '/dev/rfcomm5'
        self.port5 = '/dev/rfcomm6'
    def rfcomm0_d(self,*data):
        ser = serial.Serial(self.port0,115200,timeout=2)
        chr_open = 'b'
        cmd_open = (str(chr_open).encode('utf-8'))
        ser.write(cmd_open)
        _data = map(self.int2str,data)
        data_run = ''.join(_data)
        cmd = (str(data_run).encode('utf-8'))
        ser.write(cmd)
        chr_run = 'c'
        cmd_open = (str(chr_run).encode('utf-8'))
        ser.write(cmd_open)
        ser.flushInput()
        ser.close()
    def rfcomm1_d(self,*data):
        ser = serial.Serial(self.port1,115200,timeout=2)
        chr_open = 'b'
        cmd_open = (str(chr_open).encode('utf-8'))
        ser.write(cmd_open)
        _data = map(self.int2str,data)
        data_run = ''.join(_data)
        cmd = (str(data_run).encode('utf-8'))
        ser.write(cmd)
        chr_run = 'c'
        cmd_open = (str(chr_run).encode('utf-8'))
        ser.write(cmd_open)
        ser.flushInput()
        ser.close()
    def rfcomm2_d(self,*data):
        ser = serial.Serial(self.port2,115200,timeout=2)
        chr_open = 'b'
        cmd_open = (str(chr_open).encode('utf-8'))
        ser.write(cmd_open)
        _data = map(self.int2str,data)
        data_run = ''.join(_data)
        cmd = (str(data_run).encode('utf-8'))
        ser.write(cmd)
        chr_run = 'c'
        cmd_open = (str(chr_run).encode('utf-8'))
        ser.write(cmd_open)
        ser.flushInput()
        ser.close()
    def rfcomm3_d(self,*data):
        ser = serial.Serial(self.port3,115200,timeout=2)
        chr_open = 'b'
        cmd_open = (str(chr_open).encode('utf-8'))
        ser.write(cmd_open)
        _data = map(self.int2str,data)
        data_run = ''.join(_data)
        cmd = (str(data_run).encode('utf-8'))
        ser.write(cmd)
        chr_run = 'c'
        cmd_open = (str(chr_run).encode('utf-8'))
        ser.write(cmd_open)
        ser.flushInput()
        ser.close()
    def rfcomm4_d(self,*data):
        ser = serial.Serial(self.port4,115200,timeout=2)
        chr_open = 'b'
        cmd_open = (str(chr_open).encode('utf-8'))
        ser.write(cmd_open)
        _data = map(self.int2str,data)
        data_run = ''.join(_data)
        cmd = (chr(data_run).encode('utf-8'))
        ser.write(cmd)
        chr_run = 'c'
        cmd_open = (str(chr_run).encode('utf-8'))
        ser.write(cmd_open)
        ser.flushInput()
        ser.close()
    def rfcomm5_d(self,*data):
        ser = serial.Serial(self.port5,115200,timeout=2)
        chr_open = 'b'
        cmd_open = (str(chr_open).encode('utf-8'))
        ser.write(cmd_open)
        _data = map(self.int2str,data)
        data_run = '',join(_data)
        cmd = (str(data_run).encode('utf-8'))
        ser.write(cmd)
        chr_run = 'c'
        cmd_open = (str(chr_run).encode('utf-8'))
        ser.write(cmd_open)
        ser.flushInput()
        ser.close()
    def int2str(self,s):
        return {0:'0',1:'1',2:'2',3:'3'}[s]

    def _Thread(self,A,B,C,D,E,F):
        Thread_1 = threading.Thread(target = self.rfcomm0_d, args = A)
        Thread_2 = threading.Thread(target = self.rfcomm1_d, args = B)
        Thread_3 = threading.Thread(target = self.rfcomm2_d, args = C)
        Thread_4 = threading.Thread(target = self.rfcomm3_d, args = D)
        Thread_5 = threading.Thread(target = self.rfcomm4_d, args = E)
        Thread_6 = threading.Thread(target = self.rfcomm5_d, args = F)
        Thread_1.start()
        Thread_2.start()
        Thread_3.start()
        Thread_4.start()
        Thread_5.start()
        Thread_6.start()
    def rfcomm0(self,letter,q):
    ##    lock.acquire()
        ser = serial.Serial(self.port0,115200,timeout=2)
        if letter == 1:
            chr_open = 'a'
        elif letter == 2:
            chr_open = 's'
        cmd = (str(chr_open).encode('utf-8'))
        ser.write(cmd)
        ser.open
        voice_data_1 = float(ser.readline(2))
        print('robot_1 sensor average value:',voice_data_1)
    ##    lock.release()
        ser.flushInput()
        q.put(voice_data_1)
        #ser.close()
##        return voice_data_1
    def rfcomm1(self,letter,q):
    ##    lock.acquire()
        ser = serial.Serial(self.port1,115200,timeout=2)
        if letter == 1:
            chr_open = 'a'
        elif letter == 2:
            chr_open = 's'
        cmd = (str(chr_open).encode('utf-8'))
        ser.write(cmd)
        ser.open
        voice_data_2 = float(ser.readline(2))
        print('robot_2 sensor average value:',voice_data_2)
    ##    lock.release()
        ser.flushInput()
        q.put(voice_data_2)
        #ser.close()
##        return voice_data_2
    def rfcomm2(self,letter,q):
    ##    lock.acquire()
        ser = serial.Serial(self.port2,115200,timeout=2)
        if letter == 1:
            chr_open = 'a'
        elif letter == 2:
            chr_open = 's'
        cmd = (str(chr_open).encode('utf-8'))
        ser.write(cmd)
        ser.open
        voice_data_3 = float(ser.readline(2))
        print('robot_3 sensor average value:',voice_data_3)
    ##    lock.release()
        ser.flushInput()
        q.put(voice_data_3)
        #ser.close()
##        return voice_data_3
    def rfcomm3(self,letter,q):
    ##    lock.acquire()
        ser = serial.Serial(self.port3,115200,timeout=2)
        chr_open = 'a'
        cmd = (str(chr_open).encode('utf-8'))
        ser.write(cmd)
        ser.open
        voice_data_4 = float(ser.readline(2))
        print('robot_4 sensor average value:',voice_data_4)
    ##    lock.release()
        ser.flushInput()
        q.put(voice_data_4)
        #ser.close()
##        return voice_data_4
    def rfcomm4(self,letter,q):
    ##    lock.acquire()
        ser = serial.Serial(self.port4,115200,timeout=2)
        if letter == 1:
            chr_open = 'a'
        elif letter == 2:
            chr_open = 's'
        cmd = (str(chr_open).encode('utf-8'))
        ser.write(cmd)
        ser.open
        voice_data_5 = float(ser.readline(2))
        print('robot_5 sensor average value:',voice_data_5)
    ##    lock.release()
        ser.flushInput()
        q.put(voice_data_5)
        #ser.close()
##        return voice_data_5
    def rfcomm5(self,letter,q):
    ##    lock.acquire()
        ser = serial.Serial(self.port5,115200,timeout=2)
        if letter == 1:
            chr_open = 'a'
        elif letter == 2:
            chr_open = 's'
        cmd = (str(chr_open).encode('utf-8'))
        ser.write(cmd)
        ser.open
        voice_data_6 = float(ser.readline(2))
        print('robot_6 sensor average value:',voice_data_6)
    ##    lock.release()
        ser.flushInput()
        q.put(voice_data_6)
        #ser.close()
##        return voice_data_6
    def rfcomm2robot(self):
        q = Queue()
        try:
            _Thread_1 = threading.Thread( target = self.rfcomm0,args = (1,q))
            _Thread_2 = threading.Thread( target = self.rfcomm1,args = (1,q))
            _Thread_3 = threading.Thread( target = self.rfcomm2,args = (1,q))
            _Thread_4 = threading.Thread( target = self.rfcomm3,args = (1,q))
            _Thread_5 = threading.Thread( target = self.rfcomm4,args = (1,q))
            _Thread_6 = threading.Thread( target = self.rfcomm5,args = (1,q))
            _Thread_1.start()
            _Thread_2.start()
            _Thread_3.start()
            _Thread_4.start()
            _Thread_5.start()
            _Thread_6.start()
            _Thread_1.join()
            _Thread_2.join()
            _Thread_3.join()
            _Thread_4.join()
            _Thread_5.join()
            _Thread_6.join()
            vo1 = q.get()
            vo2 = q.get()
            vo3 = q.get()
            vo4 = q.get()
            vo5 = q.get()
            vo6 = q.get()
            
##            vo1 = self.rfcomm1(1)
##            vo2 = self.rfcomm1(1)
##            vo3 = self.rfcomm2(1)
##            vo4 = self.rfcomm3(1)
##            vo5 = self.rfcomm4(1)
##            vo6 = self.rfcomm5(1)
        except:
            print('someone robot not connect!')
        else:
            return vo1,vo2,vo3,vo4,vo5,vo6
        finally:
            print('robot data sent success!')
        

            
