
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x):
        input = x
        splitted_tensors = []
        for i in range(4):
            splitted_tensor, x = torch.split(x, [10][dim], dim)
            splitted_tensors += [splitted_tensor]
 
        # Concatenating the split tensors along axis 0 using torch.cat
        concatenated_tensor = torch.cat([splitted_tensors[i] for i in range(len(splitted_tensors))], dim=1)

        return concatenated_tensor

# Initializing the model with dim = 0, 3, or 2 
dim = 0
m = Model()
 
# Input to the model
x1 = torch.randn(4, 3*39 + 50*7)
