
class Generator(torch.nn.Module):
    def __init__(self, model_dict, **kwargs):
        super().__init__()
        self.__model_dict = dict(model_dict)

    def forward(self, x1):
        # Forward through all layers of the generator and produce a new output
        return self._forward(x1)

    def _forward(self, x1, *args):
        # Generate some output from inputs to model
        if isinstance(x1, torch.Tensor):
            return self.__model_dict['conv'](*args).view(*args)
        elif len(x1.shape) == 2:
            return self.__model_dict['deconv'](self._forward(x1.unsqueeze(0), *args))

class Model(torch.nn.Module):
    def __init__(self, generator):
        super().__init__()
        self.generator = generator
 
    def forward(self, x1):
        # Forward through all layers of the generator and produce a new output
        return self._forward(x1)

    def _forward(self, x1, *args):
        # Generate some output from inputs to model
        if isinstance(x1, torch.Tensor):
            return self.__model_dict['conv'](*args).view(*args)
        elif len(x1.shape) == 2:
            x = x1.unsqueeze(0)
            y = self.generator(x, *args)
            y = y.squeeze(0)
            y = self.__model_dict['deconv'](y)
        return y


# Initializing the model
m = Model(Generator({
    'conv': torch.nn.ConvTranspose2d(8, 3, 4, stride=2, padding=1),
    'deconv': torch.nn.Deconv2d(3, 3, 5),
    }))


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
