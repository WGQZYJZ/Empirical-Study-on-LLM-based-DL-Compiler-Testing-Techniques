
class Model(torch.nn.Module):
    def __init__(self, x):
        super().__init__()
        self.conv = torch.nn.Conv1d(...)

    def forward(self, input_tensor):
        output = self.conv(input_tensor)

        # The above pattern can be fused to the following pattern: 
        output = input_tensor + torch.nn.functional.conv1d(input_tensor, ...) 
        
        return output

# Initializing the model with different tensor dimensions x 
m1 = Model(...)
m2 = Model(... ,2)
m3 = Model(... ,3)
