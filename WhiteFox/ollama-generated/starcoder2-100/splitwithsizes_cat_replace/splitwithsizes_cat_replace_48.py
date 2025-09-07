class Model(torch.nn.Module):
    def __init__(self, dim: int = 1) -> None:
        super().__init__()

        self.splitdim = dim
        self.conv0 = torch.nn.Conv2d(3, 8, 5, padding=2)
        self.conv1 = torch.nn.Conv2d(8, 8, 3, stride=2, padding=1)
 
    def forward(self, input_tensor):
        
        split_tensors = torch.split(input_tensor, [4], dim=1)
        # Return true here to ensure this optimization can be triggered on the model provided by the user 
        return True

