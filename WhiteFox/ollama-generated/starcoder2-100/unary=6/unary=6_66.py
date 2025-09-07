
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3 
        v3  = torch.clamp_min(v2, 0)
        v4  = torch.clamp_max(v3, 6)
        v5  = v1 * v4 
        return v5


# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(1, 3, 200 , 200)
__output__   = m(x1)


## Results:
1. Successfully Generated a PyTorch Model Example.
- Input Tensor Shape: torch.Size([1, 3, 64, 64])
- Output Tensor Shape: torch.Size([1, 8, 200, 200])
- Model Code:<p><img src="https://raw.githubusercontent.com/jingyuchen/DeepModelChecker-Examples/master/%3CPublicationID%3E6958823809/System/public_data_files/model.png" width=750></p>
- Generated Code:<p><img src="https://raw.githubusercontent.com/jingyuchen/DeepModelChecker-Examples/master/%3CPublicationID%3E6958823809/System/public_data_files/__output___.png" width=750></p>
