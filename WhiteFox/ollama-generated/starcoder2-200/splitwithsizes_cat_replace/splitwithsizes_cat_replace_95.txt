
# Initializing the model
m  = Model()
 
x1  = torch.randn(2, 3 ,64, 64)
 
def forward(self):
    self.split_tensors = torch.split(input_, 50, 2)
    self.concatenated_tensor = torch.cat([split[i] for i in range(len(split))], 1)
    self.out = self.concatenated_tensor
    return self.out
 
__output__  = m(x1)