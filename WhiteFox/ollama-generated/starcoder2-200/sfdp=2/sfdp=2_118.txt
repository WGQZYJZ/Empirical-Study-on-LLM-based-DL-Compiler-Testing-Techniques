

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.randn(2, 10)
        self.key  = torch.randn(3, 4)
 
    def forward(self, x1):
         v1  = torch.matmul(self.query, self.key.transpose(-2, -1)) # Compute the dot product of a query and a key
         inv_scale_factor = float(v1[0][0]) / v1[-1].norm() * 5  # Compute an inverse scale factor as 5 times the norm of the penultimate row of the dot product divided by its first element
         inv_scale_factor /= max(2e-6, torch.finfo(torch.float32).max) # Normalize the inverse scale factor to avoid a divide by zero
         v1 = v1 / inv_scale_factor  # Divide each row of the dot product by the inverse scale factor
         v2  = v1.softmax(-1) * self.key[0]  # Compute the softmax of all the rows and then multiply them with one value
         v3  = torch.nn.functional.dropout(v2, p=0.5)
         return torch.matmul(v3, x1.transpose(-2,-1)).view_as(self.key)

# Initializing model
m  = Model()

 # Inputs to the model
x1  = torch.randn(4, 320, 798) 

 