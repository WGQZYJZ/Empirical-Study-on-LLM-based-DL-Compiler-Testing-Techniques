
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2=None):
        if x2 is None:
            t1 = x1.permute(0, 2, 1)
            v2 = torch.bmm(t1, self.linear.weight)
        else:
            t1 = input_tensor_A.permute(...) # Permute the input tensor A
            t2 = input_tensor_B.permute(...) # Permute the input tensor B
            if (x1 == None or x2 == None):
                v3 = torch.bmm(t1, t2) 
            else:
                v3 = torch.matmul(input_tensor_A, t2)

        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2) # (batch_size, channels_in, height_in, width_in)
x2 = torch.randn(1, 3, 4, 5) # (batch_size, channels_out, height_out, width_out)
