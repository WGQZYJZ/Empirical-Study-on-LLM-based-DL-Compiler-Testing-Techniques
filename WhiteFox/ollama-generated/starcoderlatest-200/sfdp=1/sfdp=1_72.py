
class Attention(torch.nn.Module):
    def __init__(self, d_model: int = 256) -> None:
        super().__init__()

        self.d_k = d_model // 8 # The output dimension of the key part in multi-head attention
        self.q_layer = torch.nn.Conv2d(3, self.d_k, 1, stride=1, padding=0)
        self.k_layer = torch.nn.Linear(64 * 64 * d_model // 8, self.d_k * self.d_k)
        self.v_layer = torch.nn.Linear(32 * 16 * d_model // 8, self.d_k * self.d_k)

        self.fc = torch.nn.Sequential()
        self.fc.add_module('flatten', torch.nn.Flatten())
        self.fc.add_module('linear', torch.nn.Linear(self.d_k * 2, d_model))

    def forward(self, x1: torch.Tensor, x2: torch.Tensor) -> torch.Tensor:
        # Get the output of each query in multi-head attention
        y = self.q_layer(x1).unsqueeze(-1).repeat((1, 1, 64, 1)) + self.k_layer(x2.view(-1, x2.shape[-1])).reshape(*x1.shape[:-1], -1)
        v = torch.tanh(y)

        # Get the output of each key in multi-head attention
        y = self.v_layer(x2).unsqueeze(-1).repeat((1, 1, 64, 1)) + x1.view(-1, self.d_k)
        v = torch.tanh(y)

        # Compute the dot product of each output with softmax and dropout
        y = torch.matmul(v, self._scale_and_apply_softmax(self._dropout(y)))
        return self._add_skips(x1, x2, y)

    def _scale_and_apply_softmax(self, tensor: torch.Tensor) -> torch.Tensor:
        # Scale and apply softmax to the dot product
        scale_factor = torch.sqrt(torch.mean((tensor ** 2), dim=[-1, -2], keepdim=True)) + 1e-6
        return self._apply_softmax(scale_factor * tensor)

    def _dropout(self, tensor: torch.Tensor) -> torch.Tensor:
        # Apply dropout to the output of softmax and dot product
        return self._apply_dropout(tensor, p=0.1)

    @staticmethod
    def _apply_softmax(tensor: torch.Tensor):
        # Apply softmax to the dot product
        scale_factor = torch.sum(tensor, dim=[-1, -2], keepdim=True) + 1e-6
        return torch.nn.functional.softmax(scale_factor * tensor, dim=-1)

    @staticmethod
    def _apply_dropout(tensor: torch.Tensor, p: float = 0.5):
        # Apply dropout to the output of softmax and dot product
        scale_factor = tensor.new_ones((tensor.shape[0], tensor.shape[-2]))
        if tensor.is_cuda():
            scale_factor = scale_factor.to(tensor)
        return torch.nn.functional.dropout(scale_factor * tensor, p=p, dim=-1)

    def _add_skips(self, x1: torch.Tensor, x2: torch.Tensor, y: torch.Tensor):
        # Add skip connections from each query in multi-head attention to the input tensor for feeding back into the transformer
        y = y + self._apply_relu(x2)
        return self._concatenate([x1, y], dim=-1)

    @staticmethod
    def _apply_relu(tensor: torch.Tensor):
        # Apply Rectified Linear Unit (ReLU) to the output of add skips and concatenate them back together
        return torch.nn.functional.relu(tensor)

    @staticmethod
    def _concatenate(tensors, dim):
        # Concatenate the tensors along a particular dimension
        for i in range(len(tensors)):
            if i != 0:
                assert tensors[i].shape[:2] == tensors[i-1].shape[:2], \
                    f'{tensors[i].shape[:2]} is not equal to {tensors[i-1].shape[:2]}'
        shape = [t.shape[:2] + (tensor_shape[-1],) for t, tensor_shape in zip(tensors, tensors[0].shape)]
        return torch.cat(tensors, dim=dim).reshape(*shape)

class Model(torch.nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.attn = Attention()
 
    def forward(self, x1: torch.Tensor, x2: torch.Tensor) -> torch.Tensor:
        y = self.attn(x1, x2)
        return y
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 64, 64)
