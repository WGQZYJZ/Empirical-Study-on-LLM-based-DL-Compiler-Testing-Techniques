
class Model(torch.nn.Module):
    def __init__(self, c1 = 32, c2=64, fc_dim = 50, dropout = 0.1):
        super().__init__()
 
        self._num_classes  =  9
        self.conv1  = torch.nn.Conv2d(c1,c2,(7,7),stride=(2,2),padding=3)
        self.bn1 = torch.nn.BatchNorm2d(c2)
        
        self.conv2 = torch.nn.Conv2d(c2,64,(5,5))
 
        self.fc0  = torch.nn.Linear(c2*7*7 + fc_dim , fc_dim//10 )
        self.drop   = torch.nn.Dropout(dropout)
        
        self._layers = [self.conv1]
        for l in [self.bn1]:
            self._layers += [l]

        self._layers += [self.fc0,torch.nn.ReLU(),self.drop,torch.nn.BatchNorm1d(5*c2*7*7),torch.nn.Linear(int(36480/4+fc_dim//10 ), 9)]
        self.model = torch.nn.Sequential(*self._layers)

    def forward(self,x):
        x  = F.max_pool2d(F.relu(self.conv1(x)),kernel_size=3,stride=2,padding=1 )

        return self.model(x)

# Initializing the model
m  = Model()

 # Inputs to the model
input1 = torch.randn([48] + [60,90])
input2 = torch.randn([48] + [30,90])


input3  =  5
input4  =  7
 
 __output__  = m(input1)

