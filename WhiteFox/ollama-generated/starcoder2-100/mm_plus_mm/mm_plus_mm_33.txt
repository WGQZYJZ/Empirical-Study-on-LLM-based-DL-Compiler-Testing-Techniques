
class Model(torch.nn.Module):
    def __init__(self, input1_size, input2_size, input3_size, input4_size):
        super().__init__()
 
        self.linear = torch.nn.Linear(input1_size + input2_size + 
                                      input3_size + input4_size)
 
    def forward(self, x1, x2, x3, x4):
         v0  = [x1]
         v1  = []
         v2  = [x3, x4]
         for i in range(len(v2)):
             v1.append(torch.mm(v0[i], self.linear(v2[i])))
 
         v3 = torch.stack(v1)
         return v3


# Initializing the model
m  = Model(input1_size=5, 
            input2_size=6,
            input3_size=7,
            input4_size=8)
            
# Inputs to the model
x1  = torch.randn(10, 5) # Matrix size (n_samples x n_features)
x2  = torch.randn(10, 6) # Matrix size (n_samples x n_features)
x3  = torch.randn(10, 7) # Matrix size (n_samples x n_features)
x4  = torch.randn(10, 8) # Matrix size (n_samples x n_features)
            
__output__   = m(x1, x2, x3, x4)

