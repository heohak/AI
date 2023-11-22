#

# var genA = function () {
#   var battery1 = flip(0.9);
#   var battery2 = flip(0.9);
#   var battery3 = flip(0.9);
#   var battery4 = flip(0.9);
#
#   // Ensure at least one battery is empty
#   var atLeastOneEmpty = !battery1 || !battery2 || !battery3 || !battery4;
#   condition(atLeastOneEmpty);
#
#   // Count how many batteries are full
#   var fullBatteries = battery1 + battery2 + battery3 + battery4;
#
#   // We're interested in the cases where exactly three batteries are full
#   return fullBatteries === 3;
# }
#
# viz(Infer({method: "enumerate"}, genA));
#
#
# var gen = function() {
#     var battery2 = flip(0.9);
#     var battery3 = flip(0.9);
#     var battery4 = flip(0.9);
#     // First battery is known to be half-empty
#     var pack = [false, battery2, battery3, battery4];
#     // Check if the remaining three batteries are full
#     return _.countBy(pack, _.identity).false === 1;
# };
#
# viz(Infer({method: "rejection", samples: 10000}, gen));
