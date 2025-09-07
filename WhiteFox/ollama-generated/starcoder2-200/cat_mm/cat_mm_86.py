
class Model(torch.nn.Module):
    def __init__(self, input1Size=32, input2Size=32):
        super().__init__()
        
        self.input1 = torch.nn.Linear(10*1568, 9)
        self.input2 = torch.nn.Conv2d(7, 4, kernel_size=(15,), padding="same", dilation=2)

    def forward(self, input):
      input1Size = input['input1'].shape[-3]
      input2Size = int((int(input1Size/8)+2)//9*7*8)
      print(f'output1: {input1Size} output2: {input2Size}')

      out1 = self.input1(input["input1"].view(-1, 30))

      out2 = self.input2(input['input2'].reshape(-1,7,8,9).permute((0,-4,1,-2,2)))
      
      return torch.cat([out1, out2])

# Initializing the model
m = Model()
# Inputs to the model
input = dict()
input["input1"]  = torch.rand(568)
input['input2'] = torch.randn((int(9*(30*7)),30*7*4,9*8))



