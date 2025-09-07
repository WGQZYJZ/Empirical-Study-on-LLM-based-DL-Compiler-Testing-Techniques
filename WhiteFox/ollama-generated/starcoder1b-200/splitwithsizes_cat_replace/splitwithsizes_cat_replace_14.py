
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 4, stride=2, padding=2)
 
    def forward(self, x):
        v1 = self.conv1(x)  # Split the input tensor into two parts: first part = input_tensor[:, :, :10, :10] and second part = input_tensor[:, :, 11:, :]
        v2 = self.conv2(torch.cat([v1[0][:, :, :5, :5], v1[1]], dim=1))  # Concatenate the two split tensors along the 1st dimension
        return torch.tanh(v2)


# Initializing the model
m = Model()
input_tensor = ...
is_valid = m.is_valid_splitwithsizes_cat(input_tensor, (5, 4))  # The model is invalid if the above condition is not met