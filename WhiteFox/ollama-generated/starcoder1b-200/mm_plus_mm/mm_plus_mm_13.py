
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1, x2) # [batch_size, num_input_channels, height, width]
        return torch.mm(v1, v1)  # [batch_size, batch_size], the output of the two matrix multiplications


# Initializing the model
m = Model()


