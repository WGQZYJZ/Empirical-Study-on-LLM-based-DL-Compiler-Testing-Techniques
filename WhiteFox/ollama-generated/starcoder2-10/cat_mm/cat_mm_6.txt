
class Model(torch.nn.Module):
    def __init__(self, n_channel):
        super().__init__()
        self.conv  = torch.nn.Conv2d(n_channel + 1 , 30, 5)
        self.acti1 = nn.ReLU()
        self.conv1= torch.nn.Conv2d(30, n_channel+1, kernel_size=5)
 
    def forward(self):
        self.conv(x)
        
# Initializing the model
m  = Model(4).to("cuda:0")

