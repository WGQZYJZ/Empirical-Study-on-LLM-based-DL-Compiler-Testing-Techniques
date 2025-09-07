
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 10)
 
    def forward(self, x2):
        l1 = self.linear(x2)
        l2 = l1 + 3
        l3 = torch.clamp_min(l2, 0)
        l4 = torch.clamp_max(l3, 6)
        l5 = l4 / 6
        return l5

# Initializing the model
m  = Model()

 # Inputs to the model
 x2  = torch.randn(1, 784).type(torch.FloatTensor)
__output__  = m(x2)

## Output tensor of your original model
__original_output__  = __output__


# Input to the model that causes a crash when fed into the previous model
__crash_input___1  = torch.randn((4097, 384)).type(torch.FloatTensor)

## Crash input 1
__crash_input__1  = __crash_input___1

 # Input to the model that causes a crash when fed into the previous model
__crash_input___2  = torch.randn((769, 4095)).type(torch.FloatTensor)
 
## Crash input 2
__crash_input__2  = __crash_input___2

 # Input to the model that causes a crash when fed into the previous model
__crash_input___3  = torch.randn((768, 4095)).type(torch.FloatTensor)
 
## Crash input 3
__crash_input__3  = __crash_input___3

 # Input to the model that causes a crash when fed into the previous model
__crash_input___4  = torch.randn((768, 2095)).type(torch.FloatTensor)
 
## Crash input 4
__crash_input__4  = __crash_input___4

 # Input to the model that causes a crash when fed into the previous model
__crash_input___5  = torch.randn((768, 2094)).type(torch.FloatTensor)
 
## Crash input 5
__crash_input__5  = __crash_input___5

 # Input to the model that causes a crash when fed into the previous model
__crash_input___6  = torch.randn((7, 2094)).type(torch.FloatTensor)
 
## Crash input 6
__crash_input__6  = __crash_input___6

 # Input to the model that causes a crash when fed into the previous model
__crash_input___7  = torch.randn((1, 2094)).type(torch.FloatTensor)
 
## Crash input 7
__crash_input__7  = __crash_input___7

 # Input to the model that causes a crash when fed into the previous model
__crash_input___8  = torch.randn((1, 2095)).type(torch.FloatTensor)
 
## Crash input 8
__crash_input__8  = __crash_input___8

 # Input to the model that causes a crash when fed into the previous model
__crash_input___9  = torch.randn((1, 4097)).type(torch.FloatTensor)
 
## Crash input 9
__crash_input__9  = __crash_input___9

 # Input to the model that causes a crash when fed into the previous model
__crash_input___10  = torch.randn((2, 4097)).type(torch.FloatTensor)
 
## Crash input 10
__crash_input__10  = __crash_input___10

 # Input to the model that causes a crash when fed into the previous model
__crash_input___11  = torch.randn((4, 769)).type(torch.FloatTensor)
 
## Crash input 11
__crash_input__11  = __crash_input___11

 # Input to the model that causes a crash when fed into the previous model
__crash_input___12  = torch.randn((4097, 5)).type(torch.FloatTensor)
 
## Crash input 12
__crash_input__12  = __crash_input___12

 # Input to the model that causes a crash when fed into the previous model
__crash_input___13  = torch.randn((4097, 5)).type(torch.FloatTensor)
 
## Crash input 13
__crash_input__13  = __crash_input___13

 # Input to the model that causes a crash when fed into the previous model
__crash_input___14  = torch.randn((78, 4096)).type(torch.FloatTensor)
 
## Crash input 14
__crash_input__14  = __crash_input___14

 # Input to the model that causes a crash when fed into the previous model
__crash_input___15  = torch.randn((78, 4096)).type(torch.FloatTensor)
 
## Crash input 15
__crash_input__15  = __crash_input___15

 # Input to the model that causes a crash when fed into the previous model
__crash_input___16  = torch.randn((78, 4097)).type(torch.FloatTensor)
 
## Crash input 16
__crash_input__16  = __crash_input___16

 # Input to the model that causes a crash when fed into the previous model
__crash_input___17  = torch.randn((2, 384)).type(torch.FloatTensor)
 
## Crash input 17
__crash_input__17  = __crash_input___17

 # Input to the model that causes a crash when fed into the previous model
__crash_input___18  = torch.randn((2, 384)).type(torch.FloatTensor)
 
## Crash input 18
__crash_input__18  = __crash_input___18

 # Input to the model that causes a crash when fed into the previous model
__crash_input___19  = torch.randn((2, 374)).type(torch.FloatTensor)
 
## Crash input 19
__crash_input__19  = __crash_input___19

 # Input to the model that causes a crash when fed into the previous model
__crash_input___20  = torch.randn((768, 4095)).type(torch.FloatTensor)
 
## Crash input 20
__crash_input__20  = __crash_input___20

 # Input to the model that causes a crash when fed into the previous model
__crash_input___21  = torch.randn((7, 4095)).type(torch.FloatTensor)
 
## Crash input 21
__crash_input__21  = __crash_input___21

 # Input to the model that causes a crash when fed into the previous model
__crash_input___22  = torch.randn((7, 4096)).type(torch.FloatTensor)
 
## Crash input 22
__crash_input__22  = __crash_input___22

 # Input to the model that causes a crash when fed into the previous model
__crash_input___23  = torch.randn((7, 4095)).type(torch.FloatTensor)
 
## Crash input 23
__crash_input__23  = __crash_input___23

 # Input to the model that causes a crash when fed into the previous model
__crash_input___24  = torch.randn((7, 5)).type(torch.FloatTensor)
 
## Crash input 24
__crash_input__24  = __crash_input___24

 # Input to the model that causes a crash when fed into the previous model
__crash_input___25  = torch.randn((768, 3095)).type(torch.FloatTensor)
 
## Crash input 25
__crash_input__25  = __crash_input___25

 # Input to the model that causes a crash when fed into the previous model
__crash_input___26  = torch.randn((7, 4096)).type(torch.FloatTensor)
 
## Crash input 26
__crash_input__26  = __crash_input___26

 # Input to the model that causes a crash when fed into the previous model
__crash_input___27  = torch.randn((4, 385)).type(torch.FloatTensor)
 
## Crash input 27
__crash_input__27  = __crash_input___27

 # Input to the model that causes a crash when fed into the previous model
__crash_input___28  = torch.randn((4096, 385)).type(torch.FloatTensor)
 
## Crash input 28
__crash_input__28  = __crash_input___28

 # Input to the model that causes a crash when fed into the previous model
__crash_input___29  = torch.randn((4096, 375)).type(torch.FloatTensor)
 
## Crash input 29
__crash_input__29  = __crash_input___29

 # Input to the model that causes a crash when fed into the previous model
__crash_input___30  = torch.randn((7, 45)).type(torch.FloatTensor)
 
## Crash input 30
__crash_input__30  = __crash_input___30

 # Input to the model that causes a crash when fed into the previous model
__crash_input___31  = torch.randn((768, 45)).type(torch.FloatTensor)
 
## Crash input 31
__crash_input__31  = __crash_input___31

 # Input to the model that causes a crash when fed into the previous model
__crash_input___32  = torch.randn((4097, 5)).type(torch.FloatTensor)
 
## Crash input 32
__crash_input__32  = __crash_input___32

 # Input to the model that causes a crash when fed into the previous model
__crash_input___33  = torch.randn((768, 4095)).type(torch.FloatTensor)
 
## Crash input 33
__crash_input__33  = __crash_input___33

 # Input to the model that causes a crash when fed into the previous model
__crash_input___34  = torch.randn((7, 5)).type(torch.FloatTensor)
 
## Crash input 34
__crash_input__34  = __crash_input___34

 # Input to the model that causes a crash when fed into the previous model
__crash_input___35  = torch.randn((768, 4095)).type(torch.FloatTensor)
 
## Crash input 35
__crash_input__35  = __crash_input___35

 # Input to the model that causes a crash when fed into the previous model
__crash_input___36  = torch.randn((7, 4095)).type(torch.FloatTensor)
 
## Crash input 36
__crash_input__36  = __crash_input___36

 # Input to the model that causes a crash when fed into the previous model
__crash_input___37  = torch.randn((4095, 12)).type(torch.FloatTensor)
 
## Crash input 37
__crash_input__37  = __crash_input___37

 # Input to the model that causes a crash when fed into the previous model
__crash_input___38  = torch.randn((4095, 12)).type(torch.FloatTensor)
 
## Crash input 38
__crash_input__38  = __crash_input___38

 # Input to the model that causes a crash when fed into the previous model
__crash_input___39  = torch.randn((4095, 12)).type(torch.FloatTensor)
 
## Crash input 39
__crash_input__39  = __crash_input___39

 # Input to the model that causes a crash when fed into the previous model
__crash_input___40  = torch.randn((768, 15)).type(torch.FloatTensor)
 
## Crash input 40
__crash_input__40  = __crash_input___40

 # Input to the model that causes a crash when fed into the previous model
__crash_input___41  = torch.randn((7, 385)).type(torch.FloatTensor)
 
## Crash input 41
__crash_input__41  = __crash_input___41

 # Input to the model that causes a crash when fed into the previous model
__crash_input___42  = torch.randn((768, 385)).type(torch.FloatTensor)
 
## Crash input 42
__crash_input__42  = __crash_input___42

 # Input to the model that causes a crash when fed into the previous model
__crash_input___43  = torch.randn((768, 5)).type(torch.FloatTensor)
 
## Crash input 43
__crash_input__43  = __crash_input___43

 # Input to the model that causes a crash when fed into the previous model
__crash_input___44  = torch.randn((7, 5)).type(torch.FloatTensor)
 
## Crash input 44
__crash_input__44  = __crash_input___44

 # Input to the model that causes a crash when fed into the previous model
__crash_input___45  = torch.randn((768, 39)).type(torch.FloatTensor)
 
## Crash input 45
__crash_input__45  = __crash_input___45

 # Input to the model that causes a crash when fed into the previous model
__crash_input___46  = torch.randn((7, 39)).type(torch.FloatTensor)
 
## Crash input 46
__crash_input__46  = __crash_input___46

 # Input to the model that causes a crash when fed into the previous model
__crash_input___47  = torch.randn((250, 39)).type(torch.FloatTensor)
 
## Crash input 47
__crash_input__47  = __crash_input___47

 # Input to the model that causes a crash when fed into the previous model
__crash_input___48  = torch.randn((250, 39)).type(torch.FloatTensor)
 
## Crash input 48
__crash_input__48  = __crash_input___48

 # Input to the model that causes a crash when fed into the previous model
__crash_input___49  = torch.randn((768, 39)).type(torch.FloatTensor)
 
## Crash input 49
__crash_input__49  = __crash_input___49

 # Input to the model that causes a crash when fed into the previous model
__crash_input___50  = torch.randn((768, 3)).type(torch.FloatTensor)
 
## Crash input 50
__crash_input__50  = __crash_input___50

 # Input to the model that causes a crash when fed into the previous model
__crash_input___51  = torch.randn((768, 3)).type(torch.FloatTensor)
 
## Crash input 51
__crash_input__51  = __crash_input___51

 # Input to the model that causes a crash when fed into the previous model
__crash_input___52  = torch.randn((7, 39)).type(torch.FloatTensor)
 
## Crash input 52
__crash_input__52  = __crash_input___52

 # Input to the model that causes a crash when fed into the previous model
__crash_input___53  = torch.randn((7, 4096)).type(torch.FloatTensor)
 
## Crash input 53
__crash_input__53  = __crash_input___53

 # Input to the model that causes a crash when fed into the previous model
__crash_input___54  = torch.randn((7, 12)).type(torch.FloatTensor)
 
## Crash input 54
__crash_input__54  = __crash_input___54

 # Input to the model that causes a crash when fed into the previous model
__crash_input___55  = torch.randn((768, 39)).type(torch.FloatTensor)
 
## Crash input 55
__crash_input__55  = __crash_input___55

 # Input to the model that causes a crash when fed into the previous model
__crash_input___56  = torch.randn((7, 4098)).type(torch.FloatTensor)
 
## Crash input 56
__crash_input__56  = __crash_input___56

 # Input to the model that causes a crash when fed into the previous model
__crash_