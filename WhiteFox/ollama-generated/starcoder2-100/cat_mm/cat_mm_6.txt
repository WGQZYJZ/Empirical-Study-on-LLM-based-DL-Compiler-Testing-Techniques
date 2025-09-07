
class Model(torch.nn.Module):
    def __init__(self, num_layer=32):
        super().__init__()
        self.conv = torch.nn.Conv2d(16, 8, 3, stride=1)
        self.fc = torch.nn.Linear(4096*num_layer, 512)
 
    def forward(self, x):
        x = self.conv(x)
        t = torch.nn.Flatten()(x)
 
        # Repeat the multiplication operation num_layer times for a matrix multiply
        t1 = t * 8  # 8 is the input dimension of the first multiplication 
        t2 = [t1] * (num_layer - 1) + [torch.mm(input1, input2)]
        t3 = torch.cat([i1 for i1 in t2], dim=0)
 
        t4 = self.fc(t3)
        return t4

# Initializing the model
m = Model()

 # Inputs to the model 
input1 = torch.rand((8,8))
input2 = torch.rand((8,512))
x = input1
__output__  = m(x)