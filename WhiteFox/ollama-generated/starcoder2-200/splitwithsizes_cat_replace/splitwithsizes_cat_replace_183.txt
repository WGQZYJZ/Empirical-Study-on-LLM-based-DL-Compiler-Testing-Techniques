
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.split = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        sp_list = [] 
        for k in [16]: 
            for j in [4096]: 
                for i in [4]: 
                    t1 = self.split(x1)
                    t2 = torch.split(t1, split_sizes=[j], dim=3)[i]
                    t3 = sp_list[k] * 0.5 + t2
                    sp_list += (t3,)
        concatenated_tensor = torch.cat([sp_list[i] for i in range(len(split_sizes))], 3)
        return __output__

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(8, 3, 4096, 257)
