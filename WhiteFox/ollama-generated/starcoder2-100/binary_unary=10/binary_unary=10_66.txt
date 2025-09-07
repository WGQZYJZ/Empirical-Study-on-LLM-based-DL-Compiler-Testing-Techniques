
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32*32*3, 10)
 
    def forward(self, x1): 
        v1  = self.linear(x1.view(-1, 32 * 32 * 3)) # Flattening the input tensor
        v2  = v1 + torch.randn_like(v1)  # Adding another random tensor to flattened output of linear transformation to form new output 
        v3  = F.relu(v2)                   # Apply ReLU activation function to flattened output from adding another random tensor  
        return v3


# Initializing the model
m  = Model() 


# Inputs to the model
x1  = torch.randn(5, 3, 32, 32)  
__output__  = m(x1)  

