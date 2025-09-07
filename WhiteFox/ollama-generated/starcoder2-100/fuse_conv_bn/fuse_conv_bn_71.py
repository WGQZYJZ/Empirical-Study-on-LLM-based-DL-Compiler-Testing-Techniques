

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input_tensor):  # This is a conv layer followed by bn layer (module API)
        v1 = torch.nn.functional.conv2d(input_tensor, 32 * [[0]]) 
        return torch.nn.functional.batchnorm2d(v1, 32, 1e-5, 0.) # This bn layer is a module


