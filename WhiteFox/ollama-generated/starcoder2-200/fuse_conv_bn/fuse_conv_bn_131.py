
class FusedConvBN(torch.nn.Module):
    def __init__(self, *args, **kwargs):
        super().__init__()

    def forward(self, x1):
        conv  = torch.nn.functional.convXd(x1)
        bn   = torch.nn.functional.batch_norm(conv)
        return bn

# Initializing the model
m  = FusedConvBN()

# Inputs to the model
input_tensor=torch.rand(2,3,480,640)
__output__  = m(input_tensor)

