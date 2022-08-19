from odoo import models
import pytz


class Website(models.Model):
    # _todo_ si può estendere Base che è più generico?
    _inherit = "base"

    def local_time(self, date_time):
        """
        return local time with user time zone if defined or UTC otherwise
        """
        try:
            user_tz = self.env.user.tz
            active_tz = pytz.timezone(user_tz) if user_tz else pytz.UTC

            return date_time.astimezone(active_tz).replace(tzinfo=None)

        except pytz.exceptions:
            return date_time

    def secs_to_hrs(self, s):
        """
        convert integer seconds in string 'H h : M m : S s' with M and S in 00 format
        """
        m, s = divmod(int(s), 60)
        h, m = divmod(m, 60)
        return "{} h : {:0>2} m : {:0>2} s".format(h, m, s)
