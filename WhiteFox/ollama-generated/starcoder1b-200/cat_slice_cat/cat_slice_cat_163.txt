
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x_list):
        v_sum = torch.cat([x[:, :, :size] for x in x_list], dim=0)
        return v_sum


# Initializing the model
m = Model()


