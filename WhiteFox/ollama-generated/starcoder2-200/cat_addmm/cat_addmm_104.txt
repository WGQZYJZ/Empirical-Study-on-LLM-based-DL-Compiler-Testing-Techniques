
class Model(torch.nn.Module):
    def __init__(self, dim1 = 256, dim2=300):
        super().__init__()

        self.fc1  = torch.nn.Linear(dim1, 4*dim2) 
        self.fc2  = torch.nn.Linear(4*dim2 + 48, 47 * 9) # Here dim1 is the number of input channels to fc1 and dim2 is the number of input channels to fc2
        self.act   = torch.nn.ReLU()
       
    def forward(self, x):
         t1 = self.fc1(x)
         t1 = torch.cat([t1], 0)
         t2 = torch.addmm(input_tensor, mat1, mat2)
         return v6


# Initializing the model
m = Model()


# Inputs to the model
input_tensor = torch.randn(batchSize * 9 * 354, 3*7)  # Input tensor of shape batchsize * dim 9 * 354 where 3 is the number of input channels for the 1st layer and 7 is the number of input channels for the 2nd layer.
mat1 = torch.randn(batchSize * 9, 80) # Input tensor mat1 with shape batchsize* dim_9 * 80 where 3 is the number of input channels to fc1
mat2 = torch.randn(47 * 9, 48) # Input tensor mat2 with shape 47*dim_9 * 48 where 47 is the number of input channels to fc1 and dim_9 is the number of input channels for the 2nd layer


