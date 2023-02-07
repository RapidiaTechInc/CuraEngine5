// Copyright (c) 2017 Ultimaker B.V.
// CuraEngine is released under the terms of the AGPLv3 or higher.

#include "SupportInfillPart.h"
#include "support.h"

using namespace cura;


SupportInfillPart::SupportInfillPart(const PolygonsPart& outline, coord_t support_line_width, size_t extruder_nr, int inset_count_to_generate)
: outline(outline)
, outline_boundary_box(outline)
, support_line_width(support_line_width)
, inset_count_to_generate(inset_count_to_generate)
, extruder_nr(extruder_nr)
{
    infill_area_per_combine_per_density.clear();
}
