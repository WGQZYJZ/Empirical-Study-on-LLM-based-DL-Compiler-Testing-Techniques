
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @staticmethod
    def drop_linear(input_tensor, num_layers=1, dropout=0., bias=True):
        return torch.nn.functional.dropout(input_tensor, p=dropout)

    @staticmethod
    def drop_batchnorm(input_tensor, eps=0., momentum=1e-3):
        return torch.nn.functional.batch_normalization(input_tensor, eps=eps, momentum=momentum)


# Initializing the model
m = Model()


