
class Model(torch.nn.Module):
    def __init__(self, model_config=None):
        super().__init__()
        if isinstance(model_config, dict) and 'nheads' in model_config:
            self.model = Transformer(
                dim=512,
                nhead=4,
                num_layers=6,
                attn_dropout=0.,
                ff_dropout=0.,
            )

        else:
            raise ValueError('ModelConfig must be of type dict or None.')

    def forward(self, x):
        output = self.model(x)
        return output


# Initializing the model
m = Model()


