
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        # input tensor in pytorch is 4D (n-dim), and the output of Conv2d is also 4D(n-dim).
        v1 = self.conv(x1) 
        # We can see that the shape of v1[0] will be 2 if the input_tensor has dimension 3.
        v2 = torch.nn.functional.batch_norm(v1)  
        return output
