
class Model(torch.nn.Module):
    def __init__(self, model_name):
        super().__init__()
        if model_name == 'pytorch':
            self.model = models.resnet18(pretrained=True)
        elif model_name == 'tensorflow':
            self.model = tfa.networks.ImageClassifierResNetV2(num_classes=5)
        else:
            raise NotImplementedError('No implemented yet!')

    def forward(self, x1):
        x2 = self.model(x1)
        