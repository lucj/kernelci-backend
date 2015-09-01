# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Model and fields for the delta/comparison."""

import models

JOB_DELTA_COMPARE_TO_VALID_KEYS = [
    models.JOB_ID_KEY,
    models.JOB_KEY,
    models.KERNEL_KEY
]

JOB_DELTA_VALID_KEYS = {
    "POST": [
        models.COMPARE_TO_KEY,
        models.JOB_ID_KEY,
        models.JOB_KEY,
        models.KERNEL_KEY
    ]
}

COMPARE_VALID_KEYS = {
    models.JOB_COLLECTION: JOB_DELTA_VALID_KEYS
}
