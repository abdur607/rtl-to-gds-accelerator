# Reconstruction and physical-design provenance

The surviving project record identifies a **16 nm FinFET cryptographic core**, an RTL-to-GDS implementation flow, resolved DRC/LVS violations, and a **228 MHz** implementation result. The original RTL, exact cipher/algorithm identity, commercial tool scripts, timing reports, layout database, and sign-off summaries were lost.

Because the exact cryptographic datapath is not recoverable, this public repository does **not** invent one and call it the historical design. Instead it contains a clearly identified **public ARX permutation surrogate** used to restore the reproducible RTL-to-GDS methodology. The historical 228 MHz result remains attached only to the lost original implementation and must not be attributed to the surrogate.

The public OpenLane/OpenROAD configuration is likewise a reproducibility path, not a statement that the historical 16 nm result was produced with an open PDK or open-source EDA.
