
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(2, 3, 3)
        self.batch_norm = torch.nn.BatchNorm2d(3)

    def forward(self, x1):
        output = self.conv1(x1)
        output = self.batch_norm(output)
        return output
# Initializing the model
m = Model()


def _get_module_params(model):
    module_params = list()
    for p in model.parameters():
        module_params.append({
            "name": str(p),
            "value": p.detach().cpu().numpy(),
        })
    return module_params
    
