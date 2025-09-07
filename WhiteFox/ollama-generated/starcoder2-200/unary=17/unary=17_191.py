class Model3(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1): # In the class definition, add a property, conv, which is a pointwise convolution
        v2  = self.conv(x1)
class Model4(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1): # In the class definition, add a property, conv, which is a pointwise convolution 
        v2  = self.conv(x1)

        v3 = v2 * torch.ones_like(v2).to(v2.device, dtype=torch.float32)
        v4 = torch.nn.Linear(80*80*3 ,50)(v2).view(-1, 64, 80, 80)
        class Model5(torch.nn.Module):
            def __init__(self, device):
                super().__init__()
 
            def forward(self, x1): # In the class definition, add a property, conv, which is a pointwise convolution 
                v2 = self.conv_relu(x1)

                v3  = nn.functional.relu(v2)
            class Model6(torch.nn.Module):

                def __init__(self, device):
                    super().__init__()
        
                def forward(self, x1):  # In the class definition, add a property, conv, which is a pointwise convolution 
                    v2 = self.conv_relu(x1)

                    v3= nn.functional.relu(v2).to('cuda:0')
            class Model7(torch.nn.Module):
                def __init__(self, device):
                    super().__init__()
        
                def forward(self, x1):  # In the class definition, add a property, conv, which is a pointwise convolution 
                    v2 = self.conv_relu(x1)

                    v3= nn.functional.relu(v2).to('cuda:0')
            class Model8(torch.nn.Module):
                def __init__(self, device):
                    super().__init__()
        
                def forward(self, x1):  # In the class definition, add a property, conv, which is a pointwise convolution 
                    v2 = self.conv_relu(x1)

                    v3= nn.functional.relu(v2).to('cuda:0')
            class Model9(torch.nn.Module):
                def __init__(self, device):
                    super().__init__()
        
                def forward(self, x1):  # In the class definition, add a property, conv, which is a pointwise convolution 
                    v2 = self.conv_relu(x1)

                    v3= nn.functional.relu(v2).to('cuda:0')
