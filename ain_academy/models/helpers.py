from odoo.exceptions import ValidationError
from odoo import fields



def _get_last_available_date(sorted_sessions):
        if sorted_sessions:
            return sorted_sessions[-1].end_date
        return fields.Datetime.now()

def _get_session_sort_key(session):
        return session.end_date



def validate_new_session(room, new_session):

        """
         Validate that the new session does not overlap with existing sessions in the same room.
         see unit test
        ########################################################
                No Overlap Should Pass                          
                                                                
                Exact Overlap Should Fail                       
                                                                
                Partial Overlap Should Fail                     
                                                                
                Same Session Should Be Ignored                  
        ########################################################
        """
        for session in room.session_ids:
                if session == new_session:
                        continue
                if session.start_date <= new_session.start_date <= session.end_date or \
                session.start_date <= new_session.end_date <= session.end_date:
                        raise ValidationError("Room already reserved during this period.")
