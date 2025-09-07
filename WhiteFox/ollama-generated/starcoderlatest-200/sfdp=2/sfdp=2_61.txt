
class Attention(torch.nn.Module):
    def __init__(self, embed_dim):
        super().__init__()
        self.matmul = torch.nn.Linear(embed_dim * 2, embed_dim)
        self.softmax = torch.nn.Softmax(dim=-1)

    def forward(self, query, key, value, scale_factor, dropout_p=0): # noqa: E501
        scaled_qk = self._scale_dot_product(query, key, scale_factor) # noqa: E501
        softmax_qk = self._apply_softmax_to_scaled_dot_product(scaled_qk) # noqa: E501
        dropout_qk = self._dropout_by_probability(softmax_qk, dropout_p) # noqa: E501
        output = self.matmul(torch.cat((query, key), dim=-1)).unsqueeze(dim=2) # noqa: E501
        return torch.nn.functional.linear(output * dropout_qk, value).squeeze() # noqa: E501

    def _scale_dot_product(self, query, key, scale_factor):  # noqa: E501
        q = self._linear(query)
        k = self._linear(key)
        return torch.matmul(q, k.transpose(-2, -1)) / scale_factor # noqa: E501

    def _apply_softmax_to_scaled_dot_product(self, scaled_qk):  # noqa: E501
        softmax_qk = self._softmax(scaled_qk) # noqa: E501
        return softmax_qk

    def _dropout_by_probability(self, dropout_q, p):  # noqa: E501
        if p == 0 or p is None:
            return dropout_q

        if isinstance(p, numbers.Number):
            if p <= 0 or p >= 1:
                raise ValueError("dropout probability has to be between 0 and 1, "
                                "but got {}".format(p))
            keep_prob = torch.empty_like(dropout_q)
            keep_prob.bernoulli_(p)
            return dropout_q * keep_prob

        if not isinstance(p, torch.Tensor):
            raise TypeError("expected probability tensor or number, but got {}"
                            .format(type(p)))
        if p.dim() != 1:
            raise ValueError("probability tensor cannot have more than one dimension")

        keep_prob = torch.empty_like(dropout_q)
        keep_prob.bernoulli_(p)
        return dropout_q * keep_prob

    def _linear(self, x):  # noqa: E501
        batch_size, embed_dim = x.shape[:2]
        linear_x = x.view(batch_size, -1)

        return self.matmul(linear_x).view(-1, embed_dim * 2)

    def _softmax(self, scaled_qk):  # noqa: E501
        attention_weights = self._apply_softmax_function(scaled_qk) # noqa: E501
        return attention_weights

    def _apply_softmax_function(self, scaled_qk):  # noqa: E501
        if scaled_qk.dim() == -1:
            softmax_qk = torch.nn.functional.softmax(scaled_qk) # noqa: E501
            return softmax_qk

        batch_size, num_heads, length, embed_dim = scaled_qk.shape

        attention_weights = torch.nn.functional.softmax(scaled_qk.view(-1, embed_dim)) # noqa: E501
        attention_weights = attention_weights.view(batch_size, num_heads, -1) # noqa: E501

        return attention_weights

class Model(torch.nn.Module):
    def __init__(self, embed_dim=64, scale_factor=2):
        super().__init__()
        self._attention = Attention(embed_dim=embed_dim)

    def forward(self, x1, x2, key, value, dropout_p=0.3): # noqa: E501
        v  = torch.cat([x1, x2], dim=-1)
        v  = self._attention(v, key, value, scale_factor=scale_factor, dropout_p=dropout_p) # noqa: E501
        v2 = v[:, 32, :, :]

        return torch.nn.functional.avg_pool2d(v2, kernel_size=(4, 4)).squeeze() # noqa: E501
# Initializing the model
m = Model(embed_dim=64, scale_factor=2)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 64, 64)
