
class Model(torch.nn.Module):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.fc1  = torch.nn.Linear(config.dim_hidden + 2 * config.dim_attention + 1, config.dim_output)
    
    @staticmethod
    def make_padding(batch_size, dim):
        return [0] * batch_size + list(range(1, 3)) + [-1] * (dim - len(query))

    @staticmethod
    def make_mask(input_size, config, mask_shape=None, padding=True):
        dim = len(input_size)
        if mask_shape is None:
            mask_shape = Model.make_padding(batch_size=config.batch_size, dim=dim) + [input_size[0] // 2] * (dim - 1)

        mask = torch.zeros(*mask_shape).to(x1.device)
        if padding:
            mask[Model.make_padding(batch_size=config.batch_size, dim=dim)] = 1

        return mask

    def forward(self, x1, x2):
        query = self.fc1(torch.cat([x1, x2], dim=-1))
        mask   = Model.make_mask(input_size=[x1.shape[0], 3], config=self.config, padding=False)

        attn = torch.matmul(query, torch.transpose(key, -2, -1).mul(value))
        attn = attn / math.sqrt(attn.shape[-1])

        return torch.sigmoid(attn)


# Initializing the model
m = Model()


