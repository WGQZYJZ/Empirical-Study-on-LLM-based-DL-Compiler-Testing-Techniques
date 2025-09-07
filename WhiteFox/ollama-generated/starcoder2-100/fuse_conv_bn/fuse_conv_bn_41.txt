
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1):
        conv = torch.nn.functional.conv3d(input1) 
        bn  = torch.nn.functional.batch_norm(conv, track_running_stats=True)
        return bn

model = Model()


# Initializing the model
model(torch.rand(20, 5, 7)) 
