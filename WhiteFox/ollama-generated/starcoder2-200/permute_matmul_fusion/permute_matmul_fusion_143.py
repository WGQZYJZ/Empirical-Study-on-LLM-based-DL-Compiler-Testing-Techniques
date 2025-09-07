
class Model(torch.nn.Module):
    def __init__(self, dim=2):
        super().__init__()

        self.linear  = torch.nn.Linear(dim + 10 * dim**2, dim)

    def forward(self, x1):

        t3a = x1.permute(0, 2, 1).permute(-1, -2)
        t4a = self.linear(t3a)
        
        t5b = x1.permute(1, 0, 2)[:, :, None].permute(0, 2, 1, 3)
        t6b = torch.nn.functional.linear(
            t5b,
            self.linear.weight[None] + [self.linear.bias[None]]
        )

        t7c = x1.permute(-2, -3)[..., None].permute(-1, 0)
        t8c = torch.nn.functional.linear(t7c, self.linear.weight, self.linear.bias)
        
        return (
            t4a + 
            t6b + 
            t8c
        )

# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(30, 5, 2).cuda().requires_grad_(True)

 # Setting gradient of the input tensor x1 to be zeros so that backpropagation does not occur.
torch.autograd.set_detect_anomaly(True); x1.requires_grad_() = False; torch.autograd.set_detect_anomaly(False); 

 