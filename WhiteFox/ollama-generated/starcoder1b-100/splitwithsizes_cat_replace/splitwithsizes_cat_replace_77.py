
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input_tensor):
        t1  = torch.nn.functional.conv2d(input_tensor, kernel_size=1)
        t2  = torch.nn.functional.conv2d(t1, kernel_size=0.5)
        t3  = torch.nn.functional.conv2d(t2, kernel_size=0.7071067811865476)
        t4  = torch.nn.functional.erf(t3)
        t5  = torch.cat([t2, t4], dim=-1) + 1
        t6  = torch.nn.functional.conv2d(t5, kernel_size=1)
        return t6


# Initializing the model
m = Model()


