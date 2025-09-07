

- The model should not have more than 2 call sites of torch methods that invoke dropout or rand_like.
- No node invoking torch method replace_fx_rand_like will be removed after its replacement, the replacement may also remove the origin torch methods.
- The size of output must match the input.