
class Model(torch.nn.Module):
    def __init__(self, other_tensor=None):
        super().__init__()
        if other_tensor:
            self.other = torch.nn.Parameter(other_tensor)
            self.linear = torch.nn.Linear(32, 16, bias=True)
            self.conv = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)
        else:
            # The model contains only one linear layer without bias and is trained with SGD optimizer, the learning rate is set to 0.5.
            self.linear = torch.nn.Linear(32, 16)
 
    def forward(self, x):
        if other_tensor:
            v1 = self.conv(x)
            v2 = self.linear(v1) + self.other
            return v2
        else:
            # The model is trained with SGD optimizer and the learning rate is set to 0.5
            v1 = self.conv(x)
            v2 = self.linear(v1)
            return v2


# Initializing the model without other tensor
m_without_other_tensor = Model()
 
# Inputs to the model without other tensor
x_without_other_tensor = torch.randn(1, 32, 32, 32)
__output_without_other_tensor__ = m_without_other_tensor(x_without_other_tensor)
 
# Initializing the model with other tensor
other_tensor = torch.randn(32, dtype=torch.float) * 0.5 + 1e-4
m_with_other_tensor = Model(other_tensor)

# Inputs to the model without other tensor
x_with_other_tensor = torch.randn(1, 8, 64, 64)
__output_with_other_tensor__ = m_with_other_tensor(x_with_other_tensor)


