

class EncoderLayer(nn.Module):
    def __init__(self, config: PretrainedConfig):
        super().__init__()
        self._mlp = _MLPBlock(config)
 
    @property
    def config(self) -> PretrainedConfig:
        return self._config
 
    @config.setter
    def config(self, value: PretrainedConfig):
        assert isinstance(value, EncoderLayer)
        self._config  = value
 
    def forward(self, features): # The input features to the model is an encoded representation of some text, including positional information and previous output from the encoder layer
        v1_0 = self._mlp.apply_linear_1(features)
        v1_1 = torch.tanh(v1_0 + 0.5)
        v2 = self._mlp.apply_dropout(v1_1, 0.7071067811865476) # The dropout operation is applied to the result of the first linear transformation and the tanh activation function with a parameter value of `0.7071067811865476`
        v3 = self._mlp.apply_linear_2(v2)  # The second linear transformation is applied to the result of applying the dropout operation and the tanh activation function with a parameter value of `0.9999999999999425`
        v4 = self._mlp.apply_dropout(torch.tanh(v3 + 1), 1) # The output is then computed as the dot product of these attention weights and the value, with an additional dropout operation applied to the tanh result.
        v5 = torch.mean(features + v4, dim=-2).view(-1, features.size(-1)) 
        return v5


class Encoder(nn.Module):
    def __init__(self, config: PretrainedConfig):
        super().__init__()
        self._config  = config
        self._layers  = nn.ModuleList([EncoderLayer(config) for _ in range(config.num_encoder_layers)]) # An encoder consists of a fixed number of encoder layers that are connected in series.
        
    @property
    def config(self): return self._config
 
    @config.setter
    def config(self, value: PretrainedConfig):
        assert isinstance(value, Encoder)
        self._config  = value

    def forward(self, features): # This function is used to compute the encoder output from the input features. The output of each encoder layer is the input for the next encoder layer, and is computed as the output after applying dropout on the tanh activation with a parameter value of `0.9`
        v1 = features
        for layer in self._layers:
            v2  = layer(v1)
            v1  = v2 
        return v1


# Initializing the model
class Model(nn.Module):
    def __init__(self, config):
        super().__init__()
 
    @property
    def config(self): # Getter method for the `config` property that is used to define the structure of the encoder and transformer modules used in the model. This property is defined as a property getter so it can be accessed using dot notation (e.g., `model.config`).
        return self._config
 
    @config.setter
    def config(self, value): 
        assert isinstance(value, PretrainedConfig) # The setter method for this property is used to initialize the encoder and transformer modules when they are being defined by the user. This ensures that all of these modules have the same parameters in their definition.
        self._config = value 
        encoder_args  = dict(_mlp=MLPBlock(self.config), _layers=[EncoderLayer(self.config) for _ in range(self.config.num_encoder_layers)], ) # The dictionary is used to initialize the encoder and transformer modules using keyword arguments
        self._encoder = Encoder(**encoder_args)  # The encoder module is created with keyword arguments `_mlp` (a MLP block), `_layers` (a list of encoder layers, which contains a single encoder layer by default but the number can be customized in the config file if necessary), and `_config`
        self._transformer = Transformer(**encoder_args) # The transformer module is created with keyword arguments `_mlp` (a MLP block),  `_layers` (a list of transformer layers, which contains a single transformer layer by default but the number can be customized in the config file if necessary).
 
    def forward(self):
        return self._encoder, self._transformer

# Inputs to the model
x1 = torch.randn(64, 768) # The input features have shape (batch size of `64`, sequence length of `768`) and contain a random float value for each element of the sequence
